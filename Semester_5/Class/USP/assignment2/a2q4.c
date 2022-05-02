/*    Name: Bali Babu Chauhan
	  Redg.no.: 19410121182
*/
#include <stdio.h>
int main(){
	int x,y,z;
	x=45;
	y=12;
	z=23;
	int *p;
	p=&x;
	printf("x=%d\n",*p);
	p=&y;
	printf("y=%d\n",*p);
	p=&z;
	printf("z=%d\n",*p);
	return 0;
}

