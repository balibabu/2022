#include <stdio.h>
int fibo(int);
int main(){
	for(int i=1;i<=5;i++)
		printf("%d ",fibo(i-1));
	printf("\n");
	return 0;
}

int fibo(int n){
	if(n==0 || n==1)
		return n;
	else
		return fibo(n-2)+fibo(n-1);
}
