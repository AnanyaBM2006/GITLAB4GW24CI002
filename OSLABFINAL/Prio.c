#include <stdio.h>

int main() {
    int n, bt[10], wt[10], tat[10], ct[10], pr[10], p[10], sum, i, j, k, pos, temp; 
    float totaltat = 0, totalwt = 0;

    printf("Enter the total number of processes: ");
    scanf("%d", &n);

    printf("\nEnter the Burst Time of each process:\n");
    for (i = 0; i < n; i++) {
        printf("Enter Burst time of process[%d]: ", i + 1);
        scanf("%d", &bt[i]);
    }

    printf("\nEnter the Priority of each process:\n");
    for (i = 0; i < n; i++) {
        printf("Enter priority of process[%d]: ", i + 1);
        scanf("%d", &pr[i]);
        p[i] = i + 1;      // Assign process number (1-based index)
    }

    // Apply Selection sort to sort according to priority
    for (i = 0; i < n; i++) {
        pos = i;
        for (j = i + 1; j < n; j++) {
            if (pr[j] < pr[pos]) {
                pos = j;
            }
        }
        // Swap priorities
        temp = pr[i];
        pr[i] = pr[pos];
        pr[pos] = temp;
        
        // Swap burst times
        temp = bt[i];
        bt[i] = bt[pos];
        bt[pos] = temp;
        
        // Swap process numbers
        temp = p[i];
        p[i] = p[pos];
        p[pos] = temp;
    }

    // Calculate completion time of processes
    sum = 0;
    for (j = 0; j < n; j++) {
        sum += bt[j];
        ct[j] = sum;
    }

    // Calculate Turn Around Time (TAT)
    for (k = 0; k < n; k++) {
        tat[k] = ct[k];
        totaltat += tat[k];
    }

    // Calculate Waiting Time (WT)
    for (k = 0; k < n; k++) {
        wt[k] = tat[k] - bt[k];
        totalwt += wt[k];
    }

    // Display results
    printf("\nProcess\tBT\tCT\tTAT\tWT\n");
    for (i = 0; i < n; i++) {
        printf("P%d\t %d\t %d\t %d\t %d\n", p[i], bt[i], ct[i], tat[i], wt[i]);
    }

    printf("\nAverage Turnaround Time: %f\n", totaltat / n);
    printf("Average Waiting Time: %f\n", totalwt / n);

    return 0;
}
