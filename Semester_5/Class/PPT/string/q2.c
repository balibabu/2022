#include <stdio.h>
void copy(char *str1,char *str2){
    //copy string from str1 to str2
    int c=0;
    for(c=0;str1[c]!='\0';c++)
        str2[c]=str1[c];
    str2[c]='\0';
}
int main(){
    char str1[100],str2[100];
    printf("enter a string\n");
    scanf("%[^\n]", str1);
    copy(str1,str2);
    printf("first string is %s\n",str1);
    printf("copied string is %s\n",str2);
    return 0;
} 