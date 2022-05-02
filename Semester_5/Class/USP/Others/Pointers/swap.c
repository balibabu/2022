#include <stdio.h>
void swap(int,int);
void swapR(int*,int*);
int main(){
	int a=5;
	int b=3;
	printf("value of a=%d and b=%d\n",a,b);
	printf("swaping with swap()\n");
	swap(a,b);
	printf("value of a=%d and b=%d\n",a,b);
	printf("swaping with swapR()\n");
	swapR(&a,&b);
	printf("value of a=%d and b=%d\n",a,b);
	return 0;
}

void swap(int a,int b){
	int temp=a;
	a=b;
	b=temp;
}
void swapR(int* a,int* b){
	int temp=*a;
	*a=*b;
	*b=temp;

}
