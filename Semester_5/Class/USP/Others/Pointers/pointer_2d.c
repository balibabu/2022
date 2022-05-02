#include <stdio.h>
int main(){
	int var=500;
	
	int* ptr1;
	int** ptr2;
	ptr1=&var;
	ptr2=&ptr1;
	
	printf("Value of var=%d and address of var is %p\n",var,&var);
	printf("Value of var using single pointer =%d and ptr1 is is %p and address of ptr1 is %p\n",*ptr1,ptr1,&ptr1);	
	printf("Value of var using double pointer =%d and ptr2 is is %p and address of ptr2 is %p\n",**ptr2,*ptr2,&ptr2);	
	return 0;
}
