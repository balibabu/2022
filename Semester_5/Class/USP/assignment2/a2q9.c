/*    Name: Bali Babu Chauhan
	  Redg.no.: 19410121182
	  Date:2021/12/10
*/
#include <stdio.h>
int main()
{
        int a=12,b=25,c=18;
        int *ptr1,*ptr2,*ptr3;
        ptr1=&a;
        *ptr1+=10;
        printf("a=%d\n",*ptr1);
        ptr2=&b;
        *ptr2+=10;
        printf("b=%d\n",*ptr2);
        ptr3=&c;
        *ptr3+=10;
        printf("c=%d\n",*ptr3);    
        return 0;
} 