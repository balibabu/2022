/*    Name: Bali Babu Chauhan
      Redg.no.: 19410121182
      Date:2021/12/13
*/
#include <stdio.h>
#include <string.h>
int main(){
    char str[50];
    int i;
    printf("enter a string\n");
    scanf("%[^\n]s", str);
    for (i=0;i<strlen(str);i++)
        printf("address of %c is %p\n",str[i],&str[i]);
    return 0;
}