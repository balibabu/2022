#include<stdio.h>
#define RATE 0.35
int main(){
	float a,b,d,cost;
	printf("MILEAGE REIMBURSEMENT CALCULATOR\n");
	printf("Enter beginning odometer reading=> ");
	scanf("%f",&a);
	printf("Enter ending odometer reading=> ");
	scanf("%f",&b);
	d=b-a;
	cost=d*RATE;
	printf("You traveled %0.1f miles. At $0.35 per mile,\n",d);
	printf("your reimbursement is $%0.2f\n",cost);
	return 0;
}