#include<stdio.h>
#include<math.h>
float celsius_at_depth(float);
float fahrenheit(float);
int main()
{
    float depth,dC,dF;
    printf("enter depth(inside earth) in km ");
    scanf("%f",&depth);
    dC=celsius_at_depth(depth);
    dF=fahrenheit(dC);
    printf("Temperatur inside earth at %.1fkm is %.1f°C or %.1f°F\n",depth,dC,dF);
    return 0;
}
float celsius_at_depth(float depth){
    return 10*depth+20;
}
float fahrenheit(float dC){
    return 1.8*dC+32;
}