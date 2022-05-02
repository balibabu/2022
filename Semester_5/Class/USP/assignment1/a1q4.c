#include <stdio.h>

int main(){

    int a=5,b=6,c=7;
    printf("a=%d,b=%d,c=%d\n",a,b,c);
    a=a+b+c;
    b=a-b-c;
    c=a-b-c;
    a=a-b-c;
    printf("a=%d,b=%d,c=%d\n",a,b,c);
    return 0;
}