#include <stdio.h>
#define ROW 2
#define COL 3
int main(){
	int i,j;
	
	int arr[ROW][COL];
	printf("enter values in array\n");
	for(i=0;i<ROW;i++){
		for(j=0;j<COL;j++){
			scanf("%d",&arr[i][j]);
		}
	}
	printf("\nvalues in array are:\n");
	for(i=0;i<ROW;i++){
		for(j=0;j<COL;j++){
			printf("%d ",arr[i][j]);
		}
		printf("\n");
	}

	return 0;
}
