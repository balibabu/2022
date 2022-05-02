#include <stdio.h>
void concatenate(char *str1,char *str2){
    //concatenate string from str2 to str1
    int i,c=0; // c is the length of str1
    for(c=0;str1[c]!='\0';c++);
    for(i=0;str2[i]!='\0';i++)
        str1[c++]=str2[i];
    str1[c]='\0';          
}
int main(){
    char str1[100],str2[100];
    printf("enter 1st string\n");
    scanf("%[^\n]s",str1);
    getchar();
    printf("enter 2nd string\n");
    scanf("%[^\n]s",str2);
    concatenate(str1,str2);
    printf("first string is %s\n",str1);
    printf("second string is %s\n",str2);
    return 0;
}