#include <stdio.h>
#include<math.h>
double natural_log(int);
int main()
{
    int x;
    printf("enter a number ");
    scanf("%d",&x);
    printf("the natural log of %d is %lf\n",x,natural_log(x));
    
    
    return 0;
} 

double natural_log(int x){
    double value=1.0*(x-1)/x;
    int i;
    for (i = 0; i < 8; i++)
    {
        value+=0.5* pow((x-1.0)/x,i+2);
    }
    return value;
}