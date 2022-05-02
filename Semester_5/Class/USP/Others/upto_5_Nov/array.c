#include<stdio.h>
#define SIZE 5
int main(){
	int i,arr[SIZE];
	printf("enter value in array\n");
	for(i=0;i<SIZE;i++){
		scanf("%d",&arr[i]);
	}
	printf("values in array are:\n");
	for(i=0;i<SIZE;i++){
		printf("%d    ",arr[i]);
	}
	printf("\n");
	return 0;
}

//array=vector
