//transpose of matrix
#define R 100
#define C 100
#include <stdio.h>
int main(){
    int mat[R][C],tmat[C][R];
    int r,c,i,j;
    printf("enter number of rows and columns\n");
    scanf("%d%d", &r,&c);
    printf("enter data for matrix\n");
    for(i=0;i<r;i++)
        for(j=0;j<c;j++){
            scanf("%d", &mat[i][j]);
            tmat[j][i]=mat[i][j];
        }

    for(i=0;i<r;i++){
        for(j=0;j<c;j++)
            printf("%d\t",mat[i][j]);
        printf("\n");
    }
    printf("\n");
    for(i=0;i<c;i++){
        for(j=0;j<r;j++)
            printf("%d\t",tmat[i][j]);
        printf("\n");
    } 
    return 0;
} 