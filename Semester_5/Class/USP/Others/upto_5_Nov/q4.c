#include <stdio.h>
int main(){
	int num,sum;
	printf("enter a number between 0 and 1000 ");
	scanf("%d",&num);
	sum=num%10;
	num=num/10;
	sum+=num%10;
	num/=10;
	sum+=num%10;
	printf("sum of digits is %d\n",sum);
	return 0;
}
