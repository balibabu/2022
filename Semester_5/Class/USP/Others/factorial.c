#include <stdio.h>
int fact(int);
int main(){
	int a;
	printf("enter a number\n");
	scanf("%d",&a);
	printf("the factorial is %d\n",fact(a));
	return 0;
}

int fact(int a){
	if(a==1 || a==0)
		return 1;
	return a*fact(a-1);
}
