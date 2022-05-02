//class in c language is struct
#include <stdio.h>
#include <stdlib.h>

typedef struct { 
    int roll;
    double x;
    char name[30];
}student1;

student1 s3;

int main()
{
    student1 s1, s2,*ptr;
  /*  ptr=(student1*)malloc(1*sizeof(student1));
    printf("enter the roll no.");
    scanf("%d",&ptr->roll);
    printf("enter enter name ");
    scanf("%s",ptr->name);
*/
    printf("enter the roll no.");
    scanf("%d",&s1.roll);
    printf("enter enter name ");
    scanf("%s",s1.name);

    ptr=&s1;
    printf("\nInfo of Students:\n\n");
    printf("Name: %s\n",ptr->name);
    printf("Roll: %d\n",ptr->roll);
    /*
    
    
    printf("enter the roll no.");
    scanf("%d",&s2.roll);
    printf("enter enter name ");
    scanf("%s",s2.name);

    printf("enter the roll no.");
    scanf("%d",&s3.roll);
    printf("enter enter name ");
    scanf("%s",s3.name);

    
    printf("\nInfo of Students:\n\n");
    printf("Name: %s\n",s1.name);
    printf("Roll: %d\n",s1.roll);

    printf("\nName: %s\n",s2.name);
    printf("Roll: %d\n",s2.roll);

    printf("\nName: %s\n",s3.name);
    printf("Roll: %d\n\n",s3.roll);

    */
    return 0;
} 