#include <stdio.h>
#include <stdlib.h>

typedef struct { 
    int roll;
    double mark;
    char name[30];
}student1;

int main(){
    student1 s;
    FILE *filepointer;
    filepointer =fopen("textBin1","r");
    fread(&s,sizeof(student1),1,filepointer);
    printf("Name:%s  Roll:%d  Mark:%lf\n",s.name,s.roll,s.mark);
    return 0;
}