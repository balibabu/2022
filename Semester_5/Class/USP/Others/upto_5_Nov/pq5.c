#include <stdio.h>
#include <math.h>
int main(){
	float v,s,t,a;
	printf("enter take off velocity of jet(km/hr) ");
	scanf("%f",&v);
	v=v*5/18;
	printf("enter run away distance(m) ");
	scanf("%f",&s);
	
	a=v*v/(2*s);
	t=sqrt(2*s/a);
	printf("acceleration of jet during takeoff is %f m/s^2\n",a);
	printf("time taken for takeoff speed is %f sec\n",t);

	return 0;
}
