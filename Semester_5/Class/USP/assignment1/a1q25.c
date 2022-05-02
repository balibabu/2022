#include <stdio.h>

int main()
{
    float x=15.0,y=25.0;
    printf("x!=y ==> %d\n",(x!=y));
    printf("x<x ==> %d\n",(x<x));
    printf("x>=y-x ==> %d\n",(x>=y-x));
    printf("x==y+x-y ==> %d\n",(x==y+x-y));
    
    return 0;
} 