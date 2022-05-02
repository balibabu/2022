/*    Name: Bali Babu Chauhan
      Redg.no.: 19410121182
      Date:2021/12/16
*/
#include <stdio.h>
#include <string.h>
char * trim_blanks(char *trimmed,const char *to_trim){
    int i=0,j=0,c=0;
    for(i=0;to_trim[i]!='\0';i++)
        if(isspace(to_trim[i])==0)
            break;
    for(j=strlen(to_trim)-1;j>i;j--)
        if(isspace(to_trim[j])==0)
            break;
    for(i;i<=j;i++){
        trimmed[c]=to_trim[i];
        c++;
    }
    trimmed[c]='\0';
    return trimmed;
}
int main(){
    char str1[50]="  hello world   ",str2[50];
    printf("%s\n",str1);
    
    printf("%s\n",trim_blanks(str2,str1));
    printf("%d\n",strlen(trim_blanks(str2,str1)));
    return 0;
} 