#include <stdio.h>
void toggle_case(char *str){
    for(int i=0;str[i]!='\0';i++){
        if(str[i]>='a' && str[i]<='z')
            str[i]-=32;
        else if(str[i]>='A' && str[i]<='Z')
            str[i]+=32;
    }
}
int main(){
    char str1[100];
    printf("enter 1st string\n");
    scanf("%[^\n]s",str1);
    toggle_case(str1);
    printf("%s\n",str1);
    
    return 0;
} 