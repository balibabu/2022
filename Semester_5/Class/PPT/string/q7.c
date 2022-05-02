#include <stdio.h>
void concatenate(char *str3,char *str1,char *str2){
    //concatenate string str1 and str2 and put it in str3
    int i,c=0;
    for(i=0;str1[i]!='\0';i++)
        str3[c++]=str1[i];
    for(i=0;str2[i]!='\0';i++)
        str3[c++]=str2[i];
    str3[c]='\0';          
}
int main(){
    char str1[100],str2[100],str3[100];
    printf("enter 1st string\n");
    scanf("%[^\n]s",str1);
    getchar();
    printf("enter 2nd string\n");
    scanf("%[^\n]s",str2);
    concatenate(str3,str1,str2);
    printf("first string is %s\n",str1);
    printf("second string is %s\n",str2);
    printf("third string is %s\n",str3);
    return 0;
}