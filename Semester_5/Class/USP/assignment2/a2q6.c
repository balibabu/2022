/*    Name: Bali Babu Chauhan
	  Redg.no.: 19410121182
	  Date:2021/12/10
*/
#include <stdio.h>
int main(){
	int x=89;
	int *p1,*p2,*p3;
	p1=&x;
	printf("x=%d\n",*p1);
	p2=&x;
	printf("x=%d\n",*p2);
	p3=&x;
	printf("x=%d\n",*p3);
	return 0;
}
