#include <stdio.h>
int main(){
    int arr[5],max,min;
    printf("Input 5 elements in the array\n");
    printf("arr[0]: ");
    scanf("%d", &arr[0]);
    max=arr[0];
    min=arr[0];
    for(int i=1;i<5;i++){
        printf("arr[%d]: ",i);
        scanf("%d", &arr[i]);
        if (arr[i]<min)
            min=arr[i];
        if (arr[i]>max)
            max=arr[i];
    }
    printf("Maximum element is: %d\n",max);
    printf("Minimum element is: %d\n",min);
    return 0;
} 

