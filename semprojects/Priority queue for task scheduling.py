import pygame
import heapq

# --- Initialization ---
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1100, 850
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Manual Preemptive Scheduler - Control Panel")
font = pygame.font.SysFont("Arial", 16, bold=True)
large_font = pygame.font.SysFont("Arial", 24, bold=True)
clock = pygame.time.Clock()

# --- Configuration ---
try:
    num_processors = int(input("Enter number of processors (1-6): "))
    num_processors = max(1, min(num_processors, 6))
except:
    num_processors = 3

# --- Global State ---
task_queue = [] 
completed_log = []
history_wait_times = [0] * 100
current_frame = 0
paused = False
input_mode = False
input_text = ""
input_stage = 0  # 0: ID, 1: Burst, 2: Priority
new_task_data = {"id": "", "burst": "", "prio": ""}

class Processor:
    def __init__(self, id):
        self.id = id
        self.name = f"Core-{id+1}"
        self.current_task = None
        self.remaining_time = 0
        self.flash = 0
        self.rect = pygame.Rect(650, 80 + (id * 90), 350, 70)

    def update(self):
        if paused: return
        if self.flash > 0: self.flash -= 1
        if self.current_task:
            self.remaining_time -= 1
            if self.remaining_time <= 0:
                completed_log.insert(0, f"{self.name}: Task {self.current_task['id']} DONE")
                if len(completed_log) > 10: completed_log.pop()
                self.current_task = None

def get_color(prio):
    if prio <= 3: return (255, 60, 60)
    if prio <= 6: return (255, 215, 0)
    return (60, 255, 60)

processors = [Processor(i) for i in range(num_processors)]

running = True
while running:
    screen.fill((18, 20, 25))
    if not paused: current_frame += 1

    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
            
            if input_mode:
                if event.key == pygame.K_RETURN:
                    if input_stage == 0: input_stage = 1
                    elif input_stage == 1: input_stage = 2
                    elif input_stage == 2:
                        # Finalize Task
                        try:
                            tid = int(new_task_data["id"])
                            burst = int(new_task_data["burst"])
                            prio = int(new_task_data["prio"])
                            heapq.heappush(task_queue, (prio, current_frame, tid, burst))
                        except: pass
                        input_mode = False
                        input_stage = 0
                        new_task_data = {"id": "", "burst": "", "prio": ""}
                elif event.key == pygame.K_BACKSPACE:
                    key = ["id", "burst", "prio"][input_stage]
                    new_task_data[key] = new_task_data[key][:-1]
                else:
                    if event.unicode.isdigit():
                        key = ["id", "burst", "prio"][input_stage]
                        new_task_data[key] += event.unicode
            else:
                if event.key == pygame.K_a:
                    input_mode = True
                    paused = True # Freeze while typing
                if event.key == pygame.K_r:
                    task_queue, completed_log, history_wait_times = [], [], [0]*100
                    for p in processors: p.current_task = None; p.remaining_time = 0

    # --- Scheduling Logic ---
    if not paused and task_queue:
        idle = [p for p in processors if p.current_task is None]
        if idle:
            prio, arr, tid, dur = heapq.heappop(task_queue)
            idle[0].current_task = {"id": tid, "prio": prio, "arr": arr}
            idle[0].remaining_time = dur
            history_wait_times.append(current_frame - arr)
        else:
            weakest = max(processors, key=lambda p: p.current_task["prio"])
            if task_queue[0][0] < weakest.current_task["prio"]:
                old = weakest.current_task
                heapq.heappush(task_queue, (old["prio"], old["arr"], old["id"], weakest.remaining_time))
                prio, arr, tid, dur = heapq.heappop(task_queue)
                weakest.current_task = {"id": tid, "prio": prio, "arr": arr}
                weakest.remaining_time = dur
                weakest.flash = 15

    # --- Drawing UI ---
    # Header
    pygame.draw.rect(screen, (30, 35, 45), (0, 0, SCREEN_WIDTH, 50))
    status_text = "PAUSED" if paused else "RUNNING"
    screen.blit(large_font.render(f"SCHEDULER: {status_text}", True, (255, 255, 255)), (20, 10))

    # Queue & Processors (Same as your design but with Names)
    for i, (p, arr, tid, dur) in enumerate(sorted(task_queue)[:10]):
        pygame.draw.rect(screen, get_color(p), (30, 95 + (i*38), 260, 32), border_radius=5)
        screen.blit(font.render(f"Task {tid} | Prio: {p}", True, (0,0,0)), (40, 100+(i*38)))

    for p in processors:
        p.update()
        col = (255,255,255) if p.flash > 0 else (get_color(p.current_task["prio"]) if p.current_task else (45, 48, 55))
        pygame.draw.rect(screen, col, p.rect, border_radius=10)
        screen.blit(font.render(p.name, True, (200, 200, 200)), (p.rect.x - 70, p.rect.y + 25))
        if p.current_task:
            txt = font.render(f"T{p.current_task['id']} (P:{p.current_task['prio']}) - {p.remaining_time} left", True, (0,0,0))
            screen.blit(txt, (p.rect.x + 20, p.rect.y + 25))

    # Manual Input Panel (Appears when 'A' is pressed)
    if input_mode:
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0,0))
        pygame.draw.rect(screen, (40, 44, 52), (350, 250, 400, 300), border_radius=15)
        
        stages = ["Enter Task ID:", "Enter Burst Time (Frames):", "Enter Priority (1-10):"]
        vals = [new_task_data["id"], new_task_data["burst"], new_task_data["prio"]]
        
        screen.blit(large_font.render("ADD NEW TASK", True, (0, 255, 255)), (460, 270))
        for idx, title in enumerate(stages):
            color = (255, 255, 255) if input_stage == idx else (100, 100, 100)
            screen.blit(font.render(title, True, color), (380, 330 + (idx * 60)))
            pygame.draw.rect(screen, (20, 20, 20), (380, 355 + (idx * 60), 340, 30))
            screen.blit(font.render(vals[idx] + ("_" if input_stage == idx else ""), True, (0, 255, 0)), (390, 360 + (idx * 60)))

    # Instructions
    instr = "[A] Add Task (Manual)   [Space] Pause/Resume   [R] Reset"
    screen.blit(font.render(instr, True, (200, 200, 200)), (20, 810))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()