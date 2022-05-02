/*
Write a program in C for a menu driven calculator having 4 functionalities Addition, Subtraction,
Multiplication and Division. All the functionalities should be implemented in functions which should
be called via function pointers.
*/

#include<stdio.h>
void sum(int a,int b);
void subtract(int a,int b);
void divide(int a,int b);
void multiply(int a,int b);
int main(){
    int a,b,choose;
    void (*funp)(int ,int);
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
				funp=&sum;
				break;
			case 2:
				funp=&subtract;
				break;
			case 3:
				funp=&divide;
				break;
			case 4:
				funp=&multiply;
				break;
			case 5:
				break;
		}   
        (*funp)(a,b);
	}while(choose!=5);
	return 0;
}
void sum(int a,int b){
	int result;
	result=a+b;
	printf("the sum of %d and %d is %d\n",a,b,result);
}
void subtract(int a,int b){
	int result;
	result=a-b;
	printf("the diff. between %d and %d is %d\n",a,b,result);
}
void divide(int a,int b){
	float result;
	result=1.0*a/b;
	printf("dividing %d by %d is %f\n",a,b,result);
}
void multiply(int a,int b){
	int result;
	result=a*b;
	printf("the product of %d and %d is %d\n",a,b,result);
}
