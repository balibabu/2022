#include <stdio.h>
int addition(int *a,int *b){
    return *a+*b;
}
int main(){
    int a,b,sum;
    printf("Input the first number : ");
    scanf("%d", &a);
    printf("Input the second number :");
    scanf("%d", &b);
    sum=addition(&a,&b);
    printf("The sum of %d and %d is %d\n",a,b,sum);
    return 0;
} 