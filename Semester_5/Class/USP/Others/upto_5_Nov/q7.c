#include <stdio.h>
#include <math.h>
int main(){
	float side,area;
	printf("enter the side of hexagon ");
	scanf("%f",&side);
	area=pow(side,2)*3*sqrt(3)/2;
	printf("area of hexagone is %f\n",area);
	return 0;
}

//while compiling use -lm
//gcc q7.c -lm
