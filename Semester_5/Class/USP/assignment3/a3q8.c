/*    Name: Bali Babu Chauhan
      Redg.no.: 19410121182
      Date:2021/12/13
*/
#include <stdio.h>
int main(){
    float a[]={1.2,5.2,1.8,1.8,1.6,4.7},*ptr1,*ptr2,*ptr3,*ptr4,*ptr5,*ptr6;
    ptr1=&a[0],ptr2=&a[1],ptr3=&a[2],ptr4=&a[3],ptr5=&a[4],ptr6=&a[5];
    printf("%f\n",*ptr1);
    printf("%f\n",*ptr2);
    printf("%f\n",*ptr3);
    printf("%f\n",*ptr4);
    printf("%f\n",*ptr5);
    printf("%f\n",*ptr6);
    return 0;
} 