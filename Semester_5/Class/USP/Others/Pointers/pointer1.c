#include <stdio.h>
int main(){
	int i=5, *p; //(*p) means value at and p is address
	
	printf("\nvalue of i is %d and its address is %p\n",i,&i);
	printf("\nvalue of p is %d and its address is %p\n",*p,p);
	p=&i;
	printf("\nAfter binding value of p is %d and its address is %p\n",*p,p);
	i++;
	printf("\n(i++) value of i is %d and its address is %p\n",i,&i);
	printf("\nvalue of p is %d and its address is %p\n",*p,p);
	(*p)++;
	printf("\nvalue of i is %d and its address is %p\n",i,&i);
	printf("\nvalue of p is %d and its address is %p\n",*p,p);
	
	return 0;
}
