#include <stdio.h>
#include <stdlib.h>
int binary_srch(int[],int,int);
int main(){
    int size,*arr,i,key;
    printf("enter size of array\n");
    scanf("%d", &size);
    arr=(int*)malloc(size*sizeof(int));
    printf("enter sorted value in array\n");
    for(i=0;i<size;i++)
        scanf("%d", &arr[i]);
    printf("enter a value to search\n");
    scanf("%d", &key);
    if(binary_srch(arr,size,key))
        printf("Yes it is present\n");
    else
        printf("No it is not present\n");
    return 0;
} 
int binary_srch(int arr[],int size,int key){
    int bottom=0,middle,top=size-1;
    while(bottom<=top){
        middle=(bottom+top)/2;
        if (arr[middle]==key)
            return 1;
        else if(arr[middle]>key)
            top=middle-1;
        else
            bottom=middle+1;
    }
    return 0;
}


// The binary search algorithm that follows may be used to search an array when the elements are in
// order. The algorithm for binary search given as;