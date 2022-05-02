
#include<stdio.h>
#include<math.h>
float speeds_ratio(int,int);
int main()
{
    int maxi,mini;
    printf("enter maximum and minimum speed in rpm ");
    scanf("%d%d",&maxi,&mini);
    printf("The ratio between successive speeds of a six-speed gearbox\nwith maximum speed %d rpm and minimum speed %d rpm\n is %.2f\n",maxi,mini,speeds_ratio(maxi,mini));
    return 0;
}
float speeds_ratio(int maxi,int mini){
    return pow(1.0*maxi/mini,1.0/5);
}