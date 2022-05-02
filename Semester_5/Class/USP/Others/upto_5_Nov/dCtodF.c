#include <stdio.h>
int main(){
	double dC,dF;
	printf("enter temp. in celcius ");
	scanf("%lf",&dC);
	dF=(9.0/5)*dC+32;
	printf("Temp. in degree Fahrenheit %lf\n",dF);

	return 0;
}
