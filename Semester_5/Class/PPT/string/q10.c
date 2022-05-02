#include <stdio.h>
#include <string.h>
void reverse(char *str){
    //reverse the same string 
    int i,l=strlen(str)-1;
    char temp;
    for (i=0;i<l;i++,l--){
        temp=str[i];
        str[i]=str[l];
        str[l]=temp;
    }
}
int main(){
    char str1[100];
    printf("enter a string\n");
    scanf("%[^\n]s",str1);
    reverse(str1);
    printf("%s\n",str1);
    
    return 0;
}  