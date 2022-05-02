#include <stdio.h>
#include <stdbool.h>
bool is_prime(int num);
int main(){
	int num;
	printf("enter a num\n");
	scanf("%d",&num);
	if(is_prime(num)){
		printf("it's a prime");
	}else{
		printf("it is not a prime");
	}
	printf("\n");
	return 0;
}

bool is_prime(int num){
	if(num<2)
		return false;
	for(int i=2;i<=num/2;i++){
		if(num%i==0){
			return false;
		}
	}
	return true;
}
