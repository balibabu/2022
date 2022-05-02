#include <stdio.h>
void copynstr_fromLast(char *str1,char *str2,int start,int end){
    //copy a part of string from str1 to str2
    int i,p=0;
    for(i=start;i<end;i++,p++)
        str2[p]=str1[i];
    str2[p]='\0';
}
int main(){
    char str1[100],str2[100];
    int start,end;
    printf("enter a string\n");
    scanf("%[^\n]", str1);
    printf("enter starting and ending point\n");
    scanf("%d%d", &start,&end);
    copynstr_fromLast(str1,str2,start,end);
    printf("first string is %s\n",str1);
    printf("copied string is %s\n",str2);
    return 0;
} 