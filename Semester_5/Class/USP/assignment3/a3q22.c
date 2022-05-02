/*    Name: Bali Babu Chauhan
      Redg.no.: 19410121182
      Date:2021/12/13
*///user defined string concatenation, comparision,copy
#include <stdio.h>
void user_strncat(char *s,char *t,int n){
    int len=0,i=0;
    for(i=0;s[i]!='\0';i++)
        len++;  //counting string length
    for(i=0;t[i]!='\0' && i<n;i++)
        s[len+i]=t[i];
}
void user_strncpy(char *s,char *t,int n){
    int i=0;
    for(i=0;t[i]!='\0' && i<n;i++)
        s[i]=t[i];
    s[i]='\0';
}
int user_strncmp(char *s,char *t,int n){
    int value=0;
    for(int i=0;i<n;i++){
        value+=s[i]-t[i];
        if(value!=0)
            return value;
    }
    return value;
}
int main(){
    char s[30]="hello",t[30]="world";
    user_strncat(s,t,3);
    printf("%s\n",s);
    user_strncpy(s,t,4);
    printf("%s\n",s);
    printf("%d\n",user_strncmp("hello","Hello",3));
    return 0;
}