#include <stdio.h>

int main()
{
    int num;
    FILE *filePointer=fopen("text.txt", "r");
    while(fscanf(filePointer,"%d",&num)!=EOF){
        printf("%d\n",num);
    }
    fclose(filePointer);
    return 0;
} 
/*
char buf[30];
while(fgets(buf,30,filePointer)!=EOF){
        printf("%s\n",buf);
    }
*/