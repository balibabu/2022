#include <stdio.h>
#include <ctype.h>
#include <string.h>
int pwd_strength(char *str1){
    int strength=0,ucase=0,lcase=0,digit=0,schar=0,i;
    char ch;
    if(strlen(str1)>=8)
        strength+=20;
    for(i=0;str1[i]!='\0';i++){
        ch=str1[i];
        if(isalnum(ch)){
            if(islower(ch) && lcase==0){
                strength+=20;
                lcase++;
            }else if(isupper(ch) && ucase==0){
                ucase++;
                strength+=20;
            }else if(isdigit(ch) && digit==0){
                digit++;
                strength+=20;
            }
        }else if(schar==0){
            strength+=20;
            schar++;
        }
    }
    return strength;
}
int main(){
    char str1[100];
    printf("enter a password\n");
    scanf("%[^\n]s",str1);
    printf("strength of your password is %d%%\n",pwd_strength(str1));
    return 0;
} 