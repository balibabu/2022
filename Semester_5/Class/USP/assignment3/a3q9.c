/*    Name: Bali Babu Chauhan
      Redg.no.: 19410121182
      Date:2021/12/13
*/
#include <stdio.h>
int main(){
    int a[]={120,502,118,188,106,447},*ptr1;
    ptr1=&a[0];
    for(int i=0;i<6;i++)
        printf("%d\n",*(ptr1+i));     
    return 0;
} 