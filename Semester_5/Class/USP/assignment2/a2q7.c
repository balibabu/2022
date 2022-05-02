/*    Name: Bali Babu Chauhan
	  Redg.no.: 19410121182
	  Date:2021/12/10
*/
#include <stdio.h>
int main(){
	float x=8.6;
	float *p1,*p2,*p3;
	p1=&x;
	printf("x=%f\n",*p1);
	p2=&x;
	printf("x=%f\n",*p2);
	p3=&x;
	printf("x=%f\n",*p3);
	return 0;
}
