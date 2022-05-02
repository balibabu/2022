#include<stdio.h>
int sum(int a,int b);
int subract(int a,int b);
float divide(int a,int b);
int multiply(int a,int b);
int main(){
int a,b,choose;
	printf("enter value of a and b ");
	scanf("%d%d",&a,&b);
	do{
		printf("make your selection\n");
		printf("1.Add\n");
		printf("2.Subtract\n");
		printf("3.Divide\n");
		printf("4.Multiply\n");
		printf("5.Exit\n");
		scanf("%d",&choose);
		switch(choose){
			case 1:
				printf("a+b=%d\n",sum(a,b));
				break;
			case 2:
				printf("a-b=%d\n",subtract(a,b));
				break;
			case 3:
				if(b==0)
					printf("error, can't divide by 0");
				else
					printf("a/b=%f\n",divide(a,b));
				break;
			case 4:
				printf("a*b=%d\n",multiply(a,b));
				break;
			case 5:
				break;
		}
	}while(choose!=5);
	return 0;
}
int sum(int a,int b){
	int result;
	result=a+b;
	return result;
}
int subtract(int a,int b){
	int result;
	result=a-b;
	return result;
}
float divide(int a,int b){
	float result;
	result=(float)a/b;
	return result;
}
int multiply(int a,int b){
	int result;
	result=a*b;
	return result;
}
