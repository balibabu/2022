#include <stdio.h>

int main()
{
    int num,sumd=0;
    printf("enter a number\n");
    scanf("%d",&num);
    while (num>0)
    {
        sumd+=num%10;
        printf("%d\n",num%10);
        
        num/=10;
    }
    if(sumd%9==0)
        printf("Yes it is divisible by 9\n");
    else
        printf("No it is not divisible by 9\n");

    return 0;
} 