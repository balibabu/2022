/*    Name: Bali Babu Chauhan
	  Redg.no.: 19410121182
*/
#include <stdio.h>
int main(){
	int a,b,temp;
	a=5;
	b=6;
	printf("a=%d and id(a)=%p\n",a,&a);
	printf("b=%d and id(b)=%p\n",b,&b);
	temp=a;
	a=b;
	b=temp;
	printf("a=%d and id(a)=%p\n",a,&a);
	printf("b=%d and id(b)=%p\n",b,&b);
	return 0;
}
