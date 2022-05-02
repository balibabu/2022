#include <stdio.h>
int is_prime();
int main(){
	int num;
	scanf("%d",&num);
	for(int i=2;i<=num;i++){
		if(is_prime(i))
			printf("%d, ",i);
	}
	printf("\n");
	
	return 0;
}

int is_prime(int num){
	if(num<=1)
		return 0;
	if(num==2 || num==3)
		return 1;
	if(num%2==0 || num%3==0)
		return 0;
	for(int i=5;i*i<=num;i+=6){
		if(num%i==0 || num%(i+2)==0)
			return 0;
	}
	return 1;
}
