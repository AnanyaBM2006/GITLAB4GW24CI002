#include <stdio.h>
#define MAX 25
int main() {
int frag[MAX], b[MAX], f[MAX], i, j, nb, nf, temp;
static int bf[MAX], ff[MAX];
printf("\n\tMemory Management Scheme - Worst Fit");
printf("\nEnter the number of blocks: ");
scanf("%d", &nb);
printf("Enter the number of files: ");
scanf("%d", &nf);
printf("\nEnter the size of the blocks:\n");
for (i = 0; i < nb; i++) {
printf("Block %d: ", i + 1);
scanf("%d", &b[i]);
bf[i] = 0; // Initialize all blocks as unallocated
}
printf("Enter the size of the files:\n");
for (i = 0; i < nf; i++) {
printf("File %d: ", i + 1);
scanf("%d", &f[i]);
}
// Allocate files to blocks using Worst Fit strategy
for (i = 0; i < nf; i++) {
int largest_block_index = -1;
for (j = 0; j < nb; j++) {
if (bf[j] == 0) { // Block is not allocated
temp = b[j] - f[i];
if (temp >= 0 && (largest_block_index == -1 || b[j] > b[largest_block_index])) {
largest_block_index = j;
}
}
}
if (largest_block_index != -1) {
ff[i] = largest_block_index;
frag[i] = b[largest_block_index] - f[i];
bf[largest_block_index] = 1; // Mark block as allocated
} else {
ff[i] = -1; // No block was found
frag[i] = -1; // Fragmentation cannot be calculated
}
}
// Print the allocation results
printf("\nFile_no:\tFile_size:\tBlock_no:\tBlock_size:\tFragment");
for (i = 0; i < nf; i++) {
printf("\n%d\t\t%d\t\t%d\t\t%d\t\t%d", i + 1, f[i], (ff[i] != -1) ? ff[i] + 1 : -1, (ff[i] != -1) ? b[ff[i]] : -1, frag[i]);
}
return 0;
}
