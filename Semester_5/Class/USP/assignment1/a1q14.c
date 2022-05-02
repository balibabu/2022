#include<stdio.h>
#include<math.h>
double get_distance(int,int,int,int,int,int);
int main()
{
    int x1,x2,y1,y2,z1,z2;
    printf("enter 1st coordinate (x1,y1,z1) ");
    scanf("%d%d%d",&x1,&y1,&z1);
    printf("enter 2nd coordinate (x2,y2,z2) ");
    scanf("%d%d%d",&x2,&y2,&z2);
    printf("distance = %lf\n",get_distance(x1,y1,z1,x2,y2,z2));
    return 0;
}
double get_distance(int x1,int y1,int z1,int x2,int y2,int z2){
    return sqrt(pow(x1-x2,2)+pow(y1-y2,2)+pow(z1-z2,2));
}