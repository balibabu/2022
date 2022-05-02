//addition of two matrix
#include <stdio.h>
#define R 100
#define C 100

int main(){
    int mat1[R][C],mat2[R][C],res[R][C];
    int r1,c1,r2,c2,i,j;
    printf("enter number of rows and columns in matrix-1\n");
    scanf("%d%d",&r1,&c1);
    printf("enter number of rows and columns in matrix-2\n");
    scanf("%d%d",&r2,&c2);
    if(!(r1==r2 && c1==c2))
        return 0;
    printf("enter data for the matrix-1\n");
    for(i=0;i<r1;i++)
        for(j=0;j<c1;j++)
            scanf("%d", &mat1[i][j]);
    printf("enter data for matrix-2\n");
    for(i=0;i<r2;i++)
        for(j=0;j<c2;j++){
            scanf("%d", &mat2[i][j]);
            res[i][j]=mat1[i][j]+mat2[i][j];
        }
    printf("matrix-1 \n");
    for(i=0;i<r2;i++){
        for(j=0;j<c2;j++)
            printf("%d ",mat1[i][j]);
        printf("\n");
        
    }
    printf("matrix-1 \n");
    for(i=0;i<r2;i++){
        for(j=0;j<c2;j++)
            printf("%d ",mat2[i][j]);
        printf("\n");
        
    }
    printf("resultant matrix is\n");  
    for(i=0;i<r2;i++){
        for(j=0;j<c2;j++)
            printf("%d ",res[i][j]);
        printf("\n");
        
    }
            
    return 0;
} 