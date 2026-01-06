#include<stdio.h>
int main()
{
 int n,at[10],bt[10],wt[10],tat[10],ct[10],sum,i,j,k; 
float totaltat=0,
totalwt=0;
printf("enter the total number of processes:"); 
scanf("%d",&n); 
printf("\nEnter The Process Arrival Time & Burst Time\n"); 
for(i=0;i<n;i++) 
{ 
printf("Enter Arrival time of process[%d]:",i+1); 
scanf("%d",&at[i]);
printf("Enter Burst time of process[%d]:",i+1); 
scanf("%d",&bt[i]); 
} 
/*Calculate completion time of processes*/ 
sum=at[0]; 
for(j=0;j<n;j++)
{ 
sum=sum+bt[j]; 
ct[j]=sum; 
} 
/*Calculate Turn Around time */ 
for(k=0; k<n;k++) 
{
tat[k]=ct[k]-at[k];
totaltat=totaltat+tat[k]; 
}
/* Calculate Waiting time */ 
for(k=0;k<n;k++) 
{
wt[k]=tat[k]-bt[k];
totalwt=totalwt+wt[k]; 
} 
printf("\n Process\t\tAT\t\tBT\t\t\tCT\t\tTAT\t\tWT\n\n"); 
for(i=0;i<n;i++) 
{ 
printf("\n P%d\t\t\t\t %d\t\t %d\t\t %d\t\t %d\t\t %d\t\t\n",i+1,at[i],bt[i],ct[i],tat[i],wt[i]); 
} 
printf("\nAverageTurnaroundTime:%f\n",totaltat/n); 
printf("\nAverage Waiting Time:%f",totalwt/n); 
return 0; 
}
