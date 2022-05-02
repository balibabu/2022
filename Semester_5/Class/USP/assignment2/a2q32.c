#include <stdio.h>
#include <stdlib.h>
void  bubble_sort(int [],int);
int main(){
    int size,*arr,i;
    printf("enter size of array\n");
    scanf("%d", &size);
    arr=(int*)malloc(size*sizeof(int));
    printf("enter value in array\n");
    for(i=0;i<size;i++)
        scanf("%d", &arr[i]);
    bubble_sort(arr,size);
    for(i=0;i<size;i++)
        printf("%d ",arr[i]);
    printf("\n");
    return 0;
} 
void  bubble_sort(int arr[],int size){
    int i,j;
    for(i=0;i<size;i++){
        for(j=i;j<size;j++){
            if (arr[i]>arr[j]){
                int temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
        }
    }
}
// The bubble sort is another technique for sorting an array. A bubble sort compares adjacent array
// elements and exchanges their values if they are out of order. In this way, the smaller values ”bubble“
// to the top of the array (toward element 0), while the larger values sink to the bottom of the array. After
// the first pass of a bubble sort, the last array element is in the correct position; after the second pass
// the last two elements are correct, and so on. Thus, after each pass, the unsorted portion of the array
// contains one less element. Write and test a function that implements this sorting method.