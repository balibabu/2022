#include <stdio.h>
#include <stdlib.h>
void multiply(int[],int[],int);
int main(){
    int size,*arr1,*arr2,i;
    printf("enter size of array\n");
    scanf("%d", &size);
    arr1=(int*)malloc(size*sizeof(int));
    arr2=(int*)malloc(size*sizeof(int));
    printf("enter value in first array\n");
    for(i=0;i<size;i++)
        scanf("%d", &arr1[i]);
    printf("enter value in 2nd array\n");
    for(i=0;i<size;i++)
        scanf("%d", &arr2[i]);   
    multiply(arr1,arr2,size);
    return 0;
} 
void multiply(int arr1[],int arr2[],int size){
    int *arr=(int*)malloc(size*sizeof(int));
    for (int i = 0; i < size; i++)
        arr[i]=arr1[i]+arr2[i];
    printf("values in result array are: \n");
    for (int i = 0; i < size; i++)
        printf("%d ",arr[i]);
    printf("\n");
}
