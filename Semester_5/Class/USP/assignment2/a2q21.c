/*  Name: Bali Babu Chauhan
    Redg.no.: 19410121182
*/
#include <stdio.h>
#include <string.h>
int main(){
    char ch[50];
    int checksum,i;
    do{
        checksum=0;
        printf("enter a sentence\n");
        scanf("%[^\n]", ch);
        getchar();
        for (i = 0; i < strlen(ch); i++)
            checksum+=(int)ch[i];
        char c=(checksum%64+(int)' ');
        // printf("%d\n",c);
        printf("the checksum is %c\n",checksum);
    }while(ch[0]!='.');
    return 0;
} 
/*
printf("enter a string\n");
    scanf("%[^.]s", string); //custom scanf
    //printf("%s\n",string);
    
    for (int i = 0; i < strlen(string); i++)
        checksum+=(int)string[i];
    char c=(checksum%65+(int)' ');
    printf("%c\n",c);
*/
