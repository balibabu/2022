#include <stdio.h>
#include "a1q24swap.c"

int main()
{
    int a=10,b=20;
    printf("Before swap in main a=%d, b=%d\n",a,b);
    swap(a,b);
    printf("after swap in main a=%d, b=%d\n",a,b);

    return 0;
} 