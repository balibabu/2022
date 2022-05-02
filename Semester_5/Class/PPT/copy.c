#include <stdio.h>
void copy(char [],char []);
int main()
{
    char src[100],dst[100];
    printf("enter a sentence\n");
    scanf("%[^\n]", src);
    copy(dst,src);
    printf("the copied data is \n%s\n",dst);
    
    return 0;
} 

void copy(char dst[],char src[]){
    int i;
    for(i=0;src[i];i++)
        dst[i]=src[i];
    dst[i]='\0';
}