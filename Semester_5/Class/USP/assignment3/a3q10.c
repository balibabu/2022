/*    Name: Bali Babu Chauhan
      Redg.no.: 19410121182
      Date:2021/12/13
*/
#include <stdio.h>
int main(){
    char a[]={'S','A','B','C','D','E'},*ptr1;
    ptr1=&a[0];
    for(int i=0;i<6;i++)
        printf("%c\n",*(ptr1+i));
    return 0;
} 