#include <stdio.h>
int main(){
	int arr[5]={1,2,3,4,5}, i=0;
	
	
	/*
	for(i=0;i<8;i++)
		printf("%d  ",*(arr+i));
	printf("\n");
*/
	for(i=0;i<8;i++)
		printf("%d  ",(arr[i]));
	printf("\n");
	
//char str[30]="hello";
//char *str="hello";
	return 0;
}
