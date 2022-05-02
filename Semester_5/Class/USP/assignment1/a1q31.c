#include <stdio.h>

int main()
{
    int decimal,binary=0,a=1;
    printf("enter a decimal number ");
    scanf("%d",&decimal);
    while (decimal>0)
    {
        binary=binary+(decimal%2)*a;
        decimal/=2;
        a*=10;
    }
    printf("%d\n",binary);
    
    
    return 0;
}