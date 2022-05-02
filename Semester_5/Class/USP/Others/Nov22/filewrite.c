#include <stdio.h>
#include <string.h>
int main()
{
    FILE *filePointer;
    char buf[30]="Data to be written in file";
    filePointer = fopen("test1.txt", "w");
    if (filePointer ==NULL){
        printf("test1.txt file failed to open\n");
    }else
    {
        printf("file is open\n");
        if (strlen(buf)>0) 
        {
            fputs(buf, filePointer);
            fputs("\n",filePointer);
        }
        
    }
    fclose(filePointer);
    printf("file is now cloosed\n");
    
    return 0;
} 