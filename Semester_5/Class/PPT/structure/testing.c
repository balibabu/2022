#include <stdio.h>
struct student{
    char a;
    char c;
    int redgno;
    char b;
};
int main(){
    printf("%d\n",sizeof(struct student));
    
    return 0;
} 