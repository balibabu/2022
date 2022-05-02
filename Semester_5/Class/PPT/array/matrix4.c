//print the diagonals
#include <stdio.h>
int main(){
    int a[3][3]={{1,2,3},{2,3,5},{6,4,3}};
    for(int i=0;i<3;i++)
        printf("%d  ",a[i][i]);
    printf("\n");
    for(int i=0;i<3;i++)
        printf("%d  ",a[3-1-i][i]);  
    printf("\n");
    return 0;
} 
// 1,2,3
// 2,3,5
// 6,4,3