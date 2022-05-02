/*    Name: Bali Babu Chauhan
	  Redg.no.: 19410121182
	  Date:2021/12/10
*/

#include <stdio.h>
int main(){
	float x,y,z;
	x=6.7;
	y=1.2;
	z=2.3;
	float *p;
	p=&x;
	printf("x=%f\n",*p);
	p=&y;
	printf("y=%f\n",*p);
	p=&z;
	printf("z=%f\n",*p);
	return 0;
}
