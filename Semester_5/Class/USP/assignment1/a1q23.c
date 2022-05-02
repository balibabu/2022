#include <stdio.h>
int getGrade(int,float,int);
int main()
{
    int hardness,tensileS;
    float carbonC;
    printf("enter hardness of steel ");
    scanf("%d",&hardness);
    printf("enter carbon content of steel ");
    scanf("%f",&carbonC);
    printf("enter tensile strength of steel ");
    scanf("%d",&tensileS);
    
   // printf("%f\n",carbonC);
    
    printf("the quality of steel is Grade %d\n",getGrade(hardness,carbonC,tensileS));
    
    
    return 0;
} 

int getGrade(int h, float c, int t){
    if(h>50 && c<0.7 && t>5600)
        return 10;
    else if(h>50 && c<0.7)
        return 9;
    else if(c<0.7 && t>5600)
        return 8;
    else if(h>50 && t>5600)
        return 7;
    else if(h>50 || c<0.7 || t>5600)
        return 6;
    else
        return 5;

}