#include <stdio.h>
#include <stdlib.h>
int main(){
    int *arr1,*arr2,size1,size2=0,i,j;
    printf("enter the size of array\n");
    scanf("%d", &size1);
    arr1=(int*)malloc(size1*sizeof(int)); 
    arr2=(int*)malloc(size1*sizeof(int)); 
    printf("enter values in array\n");
    for(i=0;i<size1;i++)
        scanf("%d", &arr1[i]);
    for(i=0;i<size1;i++){
        int c=0;
        for(j=i-1;j>=0;j--){
            if(arr1[i]==arr1[j])
                c++;
        }
        if(c==0){
            arr2[size2]=arr1[i];
            size2++;
        }
    }
    for(i=0;i<size2;i++)
        printf("%d ",arr2[i]);
    printf("\n");
    return 0;
} 