#include <stdio.h>
void copynstr(char *str1,char *str2,int n){
    //copy n chars from str1 to str2
    int i=0;
    for(i=0;i<n && str1[i]!='\0'; i++)
        str2[i]=str1[i];
    str2[i]='\0';
}
int main(){
    char str1[100],str2[100];
    int n;
    printf("enter a string\n");
    scanf("%[^\n]", str1);
    printf("enter a num upto where you wanna copy\n");
    scanf("%d", &n);
    copynstr(str1,str2,n);
    printf("first string is %s\n",str1);
    printf("copied string is %s\n",str2);
    return 0;
} 