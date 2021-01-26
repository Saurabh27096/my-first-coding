#include<stdio.h>
#define v 5
void mst(int graph[][v],int sp[][v])
{
	int i,j,min,w,y,visited[v]={0},edge,cost=0;
	edge=v-1;
	visited[0]=1;
	
	while(edge>0)
	{   min=999;
		for(i=0;i<v;i++)
		{
			for(j=0;j<v;j++)
			{   
			   if(graph[i][j]<min)
				if(visited[i]==1 &&visited[j]!=1)
				{   
					min=graph[i][j];
					w=i;y=j;
					
				}
			}
		}
	printf("from %d - %d = %d\n",w,y,min);
		visited[y]=1;  	cost+=min; edge--;
	    
	}
	printf(" Minimum cost :   %d",cost);
	
}
int main()
{
	int i,j;
	int sp[v][v];
	int graph[][v]={    { 0, 2, 0, 6, 0 },  
                        { 2, 0, 3, 8, 5 },  
                        { 0, 3, 0, 0, 7 },  
                        { 6, 8, 0, 0, 9 },  
                        { 0, 5, 7, 9, 0 }
						};
    for (i=0;i<v;i++)
       for (j=0;j<v;j++){
	   
         if (graph[i][j]==0)
             graph[i][j]=999;
         sp[i][j]=0;
	}
	
    //v=sizeof(graph)/sizeof(graph[0]);
	
/*	printf(" eneter adjecency matrix Rowwise  (its weight) :\n");
	for (i=1;i<=v;i++)
	{
		for (j=1;j<=v;j++)
		{   
		scanf("%d",&arr[i][j]);
		}
	}
*/	
mst(graph,sp);
	return 0;	
}




