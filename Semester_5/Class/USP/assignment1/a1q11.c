#include<stdio.h>
#include<stdlib.h>
int main()
{
    int m=1,n=2,side1,side2,hypotenuse;
    side1=abs(m*m-n*n);
    side2=2*m*n;
    hypotenuse=m*m+n*n;
    printf("side1=%d, side2=%d, hypotenuse=%d\n",side1,side2,hypotenuse);
    return 0;
}
