#include <stdio.h>

int main()
{
    char buf[30]="hello world";
    FILE *filepointer;
    filepointer =fopen("textBin.txt","w");
    fwrite(buf, sizeof(char),30,filepointer);
    if (fwrite!=0)
        printf("written successfully\n");
    else
        printf("error\n");
    fclose(filepointer);
    return 0;
}