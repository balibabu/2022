/*    Name: Bali Babu Chauhan
      Redg.no.: 19410121182
      Date:2021/12/16
*/
#include <stdio.h>
#include <string.h>
void bracket_by_len(char *tmp,char *str){
    if(strlen(str)<5){
        tmp[0]='<',tmp[1]='<',tmp[2]='\0';
        strcat(tmp,str);
        tmp[strlen(str)+2]='>',tmp[strlen(str)+3]='>';
        tmp[strlen(str)+4]='\0';
    }else if(strlen(str)<=10){
        tmp[0]='(',tmp[1]='*',tmp[2]='\0';
        strcat(tmp,str);
        tmp[strlen(str)+2]='*',tmp[strlen(str)+3]=')';
        tmp[strlen(str)+4]='\0';
    }else{
        tmp[0]='/',tmp[1]='+',tmp[2]='\0';
        strcat(tmp,str);
        tmp[strlen(str)+2]='+',tmp[strlen(str)+3]='/';
        tmp[strlen(str)+4]='\0';
    }
}
int main(){
    char str[50],tmp[50];
    printf("enter a string\n");
    scanf("%s", str);
    bracket_by_len(tmp,str);
    printf("%s\n",tmp);
    return 0;
} 