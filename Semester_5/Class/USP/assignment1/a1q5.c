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

/*
MILEAGE REIMBURSEMENT CALCULATOR
Enter beginning odometer reading=> 13505.2 13810.6
Enter ending odometer reading=> 13810.6
You traveled 305.4 miles. At $0.35 per mile,
your reimbursement is $106.89.
*/
