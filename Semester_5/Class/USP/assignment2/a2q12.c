/*    Name: Bali Babu Chauhan
      Redg.no.: 19410121182
      Date:2021/12/10
*/
#include <stdio.h>
int main(){
        int Ia=23;
        int *ptr1,*ptr2,*ptr3;
        ptr1=&Ia;
        *ptr1+=5;
        ptr2=&Ia;
        *ptr2+=8;
        ptr3=&Ia;
        *ptr3+=10;
        printf("a=%d\n",Ia);   
        return 0;
} 