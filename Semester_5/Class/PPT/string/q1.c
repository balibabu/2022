#include <stdio.h>
int getLength(char *string){
    //get the length of string
    int c=0;
    while(string[c]!='\0')
        c++;
    return c;
}
int main(){
    char string[100];
    printf("enter a string\n");
    scanf("%[^\n]s", string);
    
    int length=getLength(string);
    printf("%d\n",length);
    return 0;
} 