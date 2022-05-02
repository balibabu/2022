#include <stdio.h>
#include <string.h>
void substring(char *str,int start,int n){
    //extract and print the substring
    int i;
    for (i=start;i<start+n && str[i]!='\0';i++)
        printf("%c",str[i]);
}
int main(){
    char str1[100];
    int i,n;
    printf("enter a string\n");
    scanf("%[^\n]s",str1);
    printf("enter the starting point and number of characters\nnote:indexing starts from 0\n");
    scanf("%d%d", &i,&n);
    substring(str1,i,n);
    return 0;
}  