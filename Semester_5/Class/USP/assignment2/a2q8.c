/*    Name: Bali Babu Chauhan
	  Redg.no.: 19410121182
	  Date:2021/12/10
*/
#include <stdio.h>
int main()
{
        int a=12,b=25,c=18;
        int *ptr;
        ptr=&a;
        *ptr+=10;
        printf("a=%d\n",*ptr);
        ptr=&b;
        *ptr+=10;
        printf("b=%d\n",*ptr);
        ptr=&c;
        *ptr+=10;
        printf("c=%d\n",*ptr);
        return 0;
} 