/*    Name: Bali Babu Chauhan
      Redg.no.: 19410121182
      Date:2021/12/13
*/
#include <stdio.h>
int main(){
    int i,*p1,arr1[]={10,13,20,33,44};
    float *p2, arr2[]={10.2,13.3,20.0,33.3,45.3,89.9};
    p1=arr1;
    p2=arr2;
    for (i = 0; i < 5; i++)
        printf("address of %d is %p\n",*(p1+i),(p1+i));
    for (i = 0; i < 6; i++)
        printf("address of %f is %p\n",*(p2+i),(p2+i));    
    return 0;
} 