#include <stdio.h>

int main()
{
    int wspeed;
    printf("enter wind speed in (int)mph\n");
    scanf("%d",&wspeed);
    if(wspeed<25)
        printf("not a strong wind\n");
    else if(wspeed<39.54)
        printf("strong wind\n");
    else if(wspeed<55.72)
        printf("gale\n");
    else if(wspeed<72)
        printf("whole gale\n");
    else
        printf("hurricane\n");
        
    return 0;
} 