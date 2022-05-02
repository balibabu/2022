#include<stdio.h>
int main()
{
    int l1,w1,l2,w2;
    float area;
    printf("enter values in feet\n");
    printf("the length and width of a rectangular yard\n");
    scanf("%d%d",&l1,&w1);
    printf("the length and width of a rectangular house\n");
    scanf("%d%d",&l2,&w2);
    area=l1*w1-l2*w2;
    printf("time taken to cut the grass is %0.2f seconds\n",(area/2));
    return 0;
}