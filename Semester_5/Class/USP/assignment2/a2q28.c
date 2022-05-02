#include <stdio.h>
#include <math.h>
int main(){
    float sqroot[10];
    int cubes[10];
    int i=0;
    for(i=0;i<10;i++){
        sqroot[i]=sqrt(i);
        cubes[i]=pow(i,3);
    }
    printf("array of square root: ");
    for(i=0;i<10;i++)
        printf("%0.3f  ",sqroot[i]);
    printf("\n");
    printf("array of square root: ");
    for(i=0;i<10;i++)
        printf("%d  ",cubes[i]);
    printf("\n");
    return 0;
} 