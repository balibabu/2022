#include <stdio.h>
void pattern(int);
int main()
{
    pattern(5);


    return 0;
} 


void pattern(int row){
    int i,j,h,k,col=row;

    for ( i = 0; i < col; i++)
        printf("%c ",(65+i));        
    for (j = col-2; j >= 0; j--)
        printf("%c ",(65+j));
    printf("\n");

    for (k = col-2; k >=0 ; k--)
    {
        for ( i = 0; i <= k; i++)
            printf("%c ",(65+i));

        for (h = 0; h < (col-k)*2-3; h++)
            printf("  ");
        
        for (j = k; j >= 0; j--)
            printf("%c ",(65+j));

        printf("\n");
        
    }

}