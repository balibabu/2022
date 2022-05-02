#include<stdio.h>
#define PI 3.14159
int main(){
	float radius,length,area,volume;
	printf("Enter the radius and length of a cylinder: ");
	scanf("%f%f",&radius,&length);
	area = radius * radius * PI;
	volume = area * length;
	printf("The volume is %0.1f\n",volume);
	return 0;
}

