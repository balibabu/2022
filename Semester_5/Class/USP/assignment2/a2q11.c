/*    Name: Bali Babu Chauhan
      Redg.no.: 19410121182
      Date:2021/12/10
*/
#include <stdio.h>
int main(){
        int a=52,b=18;
        int *ptr1,*ptr2;
        ptr1=&a;
        ptr2=&b;
        if (*ptr1>*ptr2)
            printf("a is greater\n");
        else
            printf("b is greater\n");
        return 0;
} 