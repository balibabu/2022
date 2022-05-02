#include <stdio.h>
int factorial(int);
int isPrime(int);
int isEven(int);
int main()
{
    int num,choice;
    printf("enter a number ");
    scanf("%d",&num);
    do
    {
        printf("\nMake your choice:\n1.Factorial of a number\n2.Prime or not\n3.Odd or even\n4.Exit\n");
        scanf("%d",&choice);
        switch (choice)
        {
        case 1:
            printf("Factorial of %d is %d\n",num,factorial(num));
            break;
        case 2:
            printf("Is %d a prime? ",num);
            printf(isPrime(num) ? "Yes":"No");
            break;
        case 3:
            printf(isEven(num)? "%d is Even":"%d is Odd",num);
            break;
        case 4:
            printf("Exiting...\n");
            break;
        default:
            printf("Invalid Choice\n");
            break;
        }
        
    } while (choice!=4);
    
    return 0;
} 

int factorial(int num){
    int f=1,i;
    for (i = 1; i <=num ; i++)
        f*=i;
    return f;
}

int isPrime(int num){
    int i;
    for (i = 2; i <= num/2; i++)
    {
        if (num%i==0)
            return 0;
    }
    return 1;
}

int isEven(int num){
    return num%2==0;
}