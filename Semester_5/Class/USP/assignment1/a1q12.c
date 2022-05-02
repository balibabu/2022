#include<stdio.h>
void compute_root(double, double,double);
int main()
{
    compute_root(2,-4,-2);
    return 0;
}
void compute_root(double a, double b,double c){
    double root1,root2;
    root1=(-b+sqrt(b*b-4*a*c))/(2*a);
    root2=(-b-sqrt(b*b-4*a*c))/(2*a);
    printf("root1=%.2lf  root2=%.2lf\n",root1,root2);
}
