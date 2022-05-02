/*    Name: Bali Babu Chauhan
      Redg.no.: 19410121182
      Date:2021/12/16
*/
#include <stdio.h>
#include <string.h>
int ispalindrome(char *str){
    int size=strlen(str),i,half=strlen(str)/2;
    for(i=0;i<half;i++)
        if(str[i]!=str[size-i-1])
            return 0;
    return 1;
}
int main(){
    char str[50];
    printf("enter a string\n");
    scanf("%s", str);
    if(ispalindrome(str))
        printf("it palindrome\n");
    else
        printf("it is not palindrome\n");
    return 0;
} 