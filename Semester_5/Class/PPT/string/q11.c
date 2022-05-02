#include <stdio.h>
#include <string.h>
void reverse(char *str1,char *str2){
    //reverse the same string 
    int i,l=strlen(str1)-1;
    for(i=0;i<=l;i++)
        str2[i]=str1[l-i];
    str2[i]='\0';
    
}
int main(){
    char str1[100],str2[100];
    printf("enter a string\n");
    scanf("%[^\n]s",str1);
    reverse(str1,str2);
    printf("1st string is %s\n",str1);
    printf("2nd string is %s\n",str2);
    
    return 0;
}  