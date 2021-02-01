#include<stdio.h>

#define u 3
#define v 3

void mindis (int cost1[u][v])
{
    int m,n;
	int i,j,k,min;
	int cost2[u][v]; int visited[v][v];
	printf(" Enter row and column of second vertex:");
	scanf("%d%d",&m,&n);
	
	visited[m][n]=1;
    
	for (i=0;i<u;i++)
	{
     	for (j=0;j<v;j++)
	    {     visited[i][j]=0;
		      if ((i==m)&&(j==n))
		         cost2[i][j]=0;
		      else
		         cost2[i][j]=999;
     	}
	}
	
	for (i=m;i<u;i++)
	{
		for (j=n;j<v;j++)
		{
			if ((cost2[i][j+1] >cost1[i][j]+cost1[i][j+1])&&(j+1<u))
			{
				cost2[i][j+1] = cost1[i][j]+cost1[i][j+1];
			}
			if ((cost2[i+1][j+1] > cost1[i][j]+cost1[i+1][j+1])&&(j+1<u)&&(i+1<v))
		     	{
				cost2[i+1][j+1] = cost1[i][j]+cost1[i+1][j+1];
			   }
			if ((cost2[i][j+1] >cost1[i][j]+cost1[i][j+1])&&(i+1<v))
			   {
				cost2[i][j+1] = cost1[i][j]+cost1[i][j+1];
		     	}
		}
	}
	
	
	for (i=0;i<u;i++){
	
	  for (j=0;j<v;j++)
	  {
	  
	      printf("%d  ",cost2[i][j]);
	  }  printf("\n");
	      
	      
	  }
}


int main()
{
//	 int cost1[u][v];
	int cost1[u][v]={ 1,2,3,4,5,6,7,8,9};
	//int u=sizeof(cost1)/sizeof(cost1[0]);  printf("%d", u);
	int i,j;printf(" Enter the elements in Cost matrix: \n");
/*	
	for (i=0;i<u;i++){
	
	   for (j=0;j<v;j++)
	   {
	   
	      scanf("%d",&cost1[i][j]);
	      if (cost1[i][j]==0)
	         cost1[i][j]=999;	      
	   }
	      }
	   */   

	mindis (cost1);
	return 0;
}

