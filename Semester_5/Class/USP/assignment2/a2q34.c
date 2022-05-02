#include <stdio.h>
#include <stdlib.h>
int linear_search(const int arr[ ],int target, int n);
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
    printf("position of key is %d\n",linear_search(arr,key,size));
    return 0;
} 
int linear_search(const int arr[ ],int target, int n){
    for(int i=0;i<n;i++){
        if(arr[i]==target)
            return i;
    }
    return -1;
}

// Implement the following algorithm for linear search that sets a flag (for loop control) when the element
// being tested matches the target