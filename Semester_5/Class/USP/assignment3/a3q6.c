/*    Name: Bali Babu Chauhan
      Redg.no.: 19410121182
      Date:2021/12/13
*/
#include <stdio.h>
#include <string.h>
int main(){
    char arr1[]={'I','B','C','S','\0'};
    char arr2[]={'S','O','A','D','U'},*ptr;
    ptr=arr1;
    for (int i = 0; i < strlen(arr1); i++)
        printf("address of %c is %p\n",*(ptr+i),(ptr+i));
    ptr=arr2;
    for (int i = 0; i < strlen(arr2); i++)
        printf("address of %c is %p\n",*(ptr+i),(ptr+i));
    return 0;
} 