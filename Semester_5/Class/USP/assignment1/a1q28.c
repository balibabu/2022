#include <stdio.h>
int main()
{
    char cylinder;
    printf("enter the color of cylinder ");
    scanf("%c",&cylinder);
    
    if(cylinder=='O' || cylinder=='o')
        printf("gas cylinder contains ammonia\n");
    else if(cylinder=='B' || cylinder=='b')
        printf("gas cylinder contains carbon monoxide\n");
    else if(cylinder=='Y' || cylinder=='y')
        printf("gas cylinder contains hydrogen\n");
    else if(cylinder=='G' || cylinder=='g')
        printf("gas cylinder contains oxygen\n");
    else
        printf("Contents unknown\n");
          
    
    return 0;
} 