/*    Name: Bali Babu Chauhan
      Redg.no.: 19410121182
      Date:2021/12/13
*/
#include <stdio.h>
#include <string.h>
#include <ctype.h>
int main(){
    char str[]="ITER-IBCS-ABD";
    char ptr[]="iter-ibcs-abd";
    char *token,*ptoken;
    token=strtok(str,"-");
    ptoken=strtok(ptr,"-");
    while(token!=NULL){
        printf("%s\n",token);
        token=strtok(NULL,"-");
        
    }
    return 0;
} 