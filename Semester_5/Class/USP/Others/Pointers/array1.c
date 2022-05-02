#include <stdio.h>
int main(){
	int arr[5]={1,2,3,4,5}, i=0, *ptr;
	printf("only arr is %p and address of arr[0] is %p\n",arr,&arr[0]);
	
	ptr=arr;

	printf("printing array using ptr=arr and ptr[i]\n");
	for(i=0;i<5;i++)
		printf("%d  ",ptr[i]);
	printf("\n");

	printf("printing array using ptr=arr , ptr++ and *ptr\n");
	i=0;
	for(ptr=arr;i<5;i++,ptr++)
		printf("%d  ",*ptr);
	printf("\n");
		
	printf("printing array using ptr=arr and *(ptr+i)\n");
	for(i=0;i<5;i++)
		printf("%d  ",*(ptr+i));
	printf("\n");
		
	return 0;
}
