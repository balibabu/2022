#include <stdio.h>
#include <stdlib.h>

typedef struct { 
    int roll;
    double mark;
    char name[30];
}student1;

int main(){
    FILE *filepointer;
    filepointer =fopen("textBin1","w");
    student1 s;
    printf("enter your name\n");
    scanf("%s",s.name);
    printf("enter your roll\n");
    scanf("%d",&s.roll);
    printf("enter your mark\n");
    scanf("%lf",&s.mark);
    
    fwrite(&s, sizeof(s),1,filepointer);
    if (fwrite!=0)
        printf("written successfully\n");
    else
        printf("error\n");
    fclose(filepointer);

    return 0;
}