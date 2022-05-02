#include <stdio.h>
struct student1{
    char a,b;
    int redgno;
    char d,e,f;
};

struct student2{
    char a,b;
    int redgno;
    char d,e,f;
} __attribute__ ((__packed__));

struct student3{
    double m;
    char a;
    int redgno;
    
};

int main(){
    printf("%d\n",sizeof(struct student1));
    printf("%d\n",sizeof(struct student2));
    printf("%d\n",sizeof(struct student3));

    return 0;
}    












