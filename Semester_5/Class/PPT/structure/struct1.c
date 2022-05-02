#include <stdio.h>
struct student{
    int redgno;
    char name[30];
    char branch[5];
    int sem;
    float cgpa;
};


struct student s1; //this is global
int main(){
    // //structure definition, It allocates moemory as per the declaration
    // struct student s2; //this is local  also s is implicit pointer
    // printf("enter student data\n");
    // scanf("%d %[^\n] %s %d %f",&s2.redgno,s2.name,s2.branch,&s2.sem,&s2.cgpa);
    // printf("%d  %s  %s  %d  %f\n",s2.redgno,s2.name,s2.branch,s2.sem,s2.cgpa);
    

    struct student temp={1941,"bali babu","cse",5,8.1};
    printf("%d  %s  %s  %d  %f\n",temp.redgno,temp.name,temp.branch,temp.sem,temp.cgpa);
    
    // struct student *s3; //explicit pointer
    // s3=(struct student *)malloc(sizeof(struct student));
    // printf("enter student data\n");
    // scanf("%d %[^\n] %s %d %f",&s3->redgno,s3->name,s3->branch,&s3->sem,&s3->cgpa);
    // printf("%d  %s  %s  %d  %f\n",s3->redgno,s3->name,s3->branch,s3->sem,s3->cgpa);
    

    // struct student s4[5]; //array of structure


    return 0;
} 