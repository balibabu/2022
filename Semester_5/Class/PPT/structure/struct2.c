#include <stdio.h>
struct student{
    int redgno;
    char name[30];
    char branch[5];
    int sem;
    float cgpa;
};

int main(){
    int i;
    struct student s1[2]; //array of structure
    struct student *s2;
    s2=(struct student *)malloc(2*sizeof(struct student));
    for(i=0;i<2;i++){
        printf("enter student data\n");
        scanf("%d %[^\n] %s %d %f",&(s2+i)->redgno,(s2+i)->name,(s2+i)->branch,&(s2+i)->sem,&(s2+i)->cgpa);
    }
    for(i=0;i<2;i++){
        printf("student data %d\n",i);
        printf("%d %s %s %d %f\n",(s2+i)->redgno,(s2+i)->name,(s2+i)->branch,(s2+i)->sem,(s2+i)->cgpa);
    }
    return 0;
