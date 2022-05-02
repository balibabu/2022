#include<stdio.h>
#include<math.h>
double thirdsidecompute(int, int, int);
int main()
{
    int b,c,angle;
    printf("enter length of two sides and angle between them\n");
    scanf("%d%d%d",&b,&c,&angle);
    printf("the third side of triangle is %0.2lf\n",thirdsidecompute(b,c,angle));
    return 0;
}
double thirdsidecompute(int b, int c, int angle){
    double a=sqrt(b*b+c*c-2.0*b*c*cos(angle*M_PI/180));
    return a;
}