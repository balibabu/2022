#include <stdio.h>
#include <string.h>
int main()
{
    FILE *filePointer;
    filePointer=fopen("test1.txt","r");
    char buf[30];
    while (fgets(buf,30,filePointer)!=NULL){
        printf("%s\n",buf);  
    }
    fclose(filePointer);
    return 0;
} 