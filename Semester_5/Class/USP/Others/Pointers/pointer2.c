#include <stdio.h>
#include <stdlib.h>
int main(){
	int* p=(int*)malloc(2*sizeof(int));
	int size,i;
	printf("Enter size of array ");
	scanf("%d",&size);
	//p=(int*)malloc(size*sizeof(int)); //calloc,realloc,
	realloc(p,size); //returns some value //p=realloc(p,size); /also works
	for(i=0;i<size;i++){
		printf("enter pointer element for index %d\n",i);
		scanf("%d",&p[i]);
	}
	printf("entered numbers are\n");
	for(i=0;i<size;i++){
		printf("Pointer element at index %d is %d\n",i,p[i]);
	}
	free(p);
	return 0;
}
