/*    Name: Bali Babu Chauhan
      Redg.no.: 19410121182
      Date:2021/12/13
*/
#include <stdio.h>
#include <string.h>
void stringconcate(char *s,char *t){
    int len=strlen(s);
    for(int i=0;t[i]!='\0';i++)
        s[len+i]=t[i];
}
int main(){
    char s[30]="hello",t[30]="world";
    stringconcate(s,t);
    printf("%s\n",s);
    return 0;
}   