#include <stdio.h>
#include <string.h>
int ispalindrome(char *str){
    //is it palindrome
    int i,l=strlen(str)-1;
    char temp;
    for (i=0;i<l;i++,l--)
        if(str[i]!=str[l])
            return 0;
    return 1;
}
int main(){
    char str1[100];
    printf("enter a string\n");
    scanf("%[^\n]s",str1);
    if(ispalindrome(str1))
        printf("It is palindrome\n");
    else
        printf("it is not palindrome");
    
    return 0;
}  