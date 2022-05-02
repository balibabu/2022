#include <stdio.h>
void pointer_to_constant();
void constant_pointer();
int main()
{
    
    pointer_to_const();
    constant_pointer();
    return 0;
}
void pointer_to_constant(){
    const int x=9;
    int y=5;
    const int *p;
    int *q;
    //p=&x;
    p=&y;
    y++;
    q=&x;
    (*q)++;
    printf("%d\n",*p);
    printf("%d\n",*q);
    printf("%d\n",x);
}
