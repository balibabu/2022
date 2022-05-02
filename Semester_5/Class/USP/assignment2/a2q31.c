#include <stdio.h>
#include <stdlib.h>
int  find_largest(int [],int);
int main()
{
    int size,*arr,i;
    printf("enter size of array\n");
    scanf("%d", &size);
    arr=(int*)malloc(size*sizeof(int));
    printf("enter value in array\n");
    for(i=0;i<size;i++)
        scanf("%d", &arr[i]);
    printf("the largest element is %d\n",find_largest(arr,size));
    return 0;
} 
int  find_largest(int arr[],int size){
    int i,max=arr[0];
    for(i=1;i<size;i++){
        if(arr[i]>max)
            max=arr[i];
    }
    return max;
}