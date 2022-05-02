#include <stdio.h>

int main()
{
    int num;
    printf("Enter an integer ");
    scanf("%d",&num);
    printf("is %d divisible by 5 and 6? ");
    if (num%5==0 && num%6==0)  
        printf("True\n");
    else
        printf("False\n");
    printf("is %d divisible by 5 or 6? ");
    if (num%5==0 || num%6==0)  
        printf("True\n");
    else
        printf("False\n");
    printf("is %d divisible by 5 or 6 but not both? ");
    if (num%5==0 ^ num%6==0)  
        printf("True\n");
    else
        printf("False\n");
} 