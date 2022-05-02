#include <stdio.h>
#include <math.h>
int main()
{
    float array[]={15.3,4,90,34,2.5,104,7,25,82};
    float average;
    int i=0;
    for (i = 0; i < sizeof(array)/sizeof(1); i++)
        average+=array[i];
    average/=(sizeof(array)/sizeof(1));
    printf("Mean=%f\n",average);
    float sum=0,sd=0;
    for (i = 0; i < sizeof(array)/sizeof(1); i++)
        sum+=pow((array[i]-average),2);
    sd=sqrt(sum/(sizeof(array)/sizeof(1))); //this is valid for population and for sample we need to divide by n-1
    printf("sdandard deviation=%f\n",sd);
    return 0;
} 