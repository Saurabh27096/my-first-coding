#include<stdio.h>
#define v 5
void dijkastra(int cost1[][v],int u)
{   int i,j,z;
printf("Enter the source node:  ");
scanf("%d",&z);
    
    int cost2[v],visited[v]={0};
   		for (i=0;i<v;i++)
   		   {
   		   	if(i==z)
   		   	  cost2[i]=0;
   		   	else
   		   	   cost2[i]=999;
	    	}
	visited[z]=1;
	int k;
	for (k=0;k<v;k++)
	{
	
		for (j=0;j<v;j++)
		{
			if ((cost2[j]>((cost1[z][j]))+cost2[z])&&(visited[j]!=1))
			  {
			  	cost2[j]=cost2[z]+cost1[z][j];
			  }
		}
		int min=999;
		for(i=0;i<v;i++)
		{
			if ((cost2[i]<min)&&(visited[i]==0))
			    z=i;
		}
		visited[z]=1;
	}
	for (i=0;i<v;i++)
	     printf("%d   ",cost2[i]);	
}
int main()
{
	int cost1[][v]={ 0 ,5, 10, 2, 0, 5, 0, 3, 7, 2, 10, 3, 0, 0, 0, 2, 7, 0, 0, 3, 0, 2, 0, 3, 0};
	int u=sizeof(cost1)/sizeof(cost1[0]);  printf("%d", u);
	int i,j;
	for (i=0;i<u;i++)
	{
		for (j=0;j<v;j++)
		{
			if(cost1[i][j]==0)
			   cost1[i][j]=999;
		}
	}
	dijkastra(cost1,u);
}
