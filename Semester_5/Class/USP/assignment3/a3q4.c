/*    Name: Bali Babu Chauhan
      Redg.no.: 19410121182
      Date:2021/12/13
*/
#include <stdio.h>
int main(){
    int a[]={0,10,20,30,40,50,60,70,80,90};
    for(int i=0;i<10;i++)
        printf("address of %d is %p\n",a[i],&a[i]);
    return 0;
} 