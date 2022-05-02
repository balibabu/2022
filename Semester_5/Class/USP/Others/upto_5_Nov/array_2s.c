#include <stdio.h>
#define ROW1 2
#define COL1 3

#define ROW2 2
#define COL2 3
int main(){
	int i,j,arr1[ROW1][COL1],arr2[ROW2][COL2];
	printf("enter values in 1st array\n");
	for(i=0;i<ROW1;i++){
		for(j=0;j<COL1;j++){
			scanf("%d",&arr1[i][j]);
		}
	}
	
	printf("enter values in 2nd array\n");
	for(i=0;i<ROW2;i++){
		for(j=0;j<COL2;j++){
			scanf("%d",&arr2[i][j]);
		}
	}
	
	
	printf("\nvalues in 1st array are:\n");
	for(i=0;i<ROW1;i++){
		for(j=0;j<COL1;j++){
			printf("%d ",arr1[i][j]);
		}
		printf("\n");
	}
	
	printf("\nvalues in 2nd array are:\n");
	for(i=0;i<ROW2;i++){
		for(j=0;j<COL2;j++){
			printf("%d ",arr2[i][j]);
		}
		printf("\n");
	}

	return 0;
}
