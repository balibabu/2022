#include <stdio.h>
#include <stdlib.h>
int main()
{
    printf("hello\n");
    
    int arr[10],i,size=2;
    //arr=(int*)malloc(size*sizeof(int));
    printf("%d\n",sizeof(arr));
    for(i=0;i<10;i++){
        arr[i]=i;
    }
    

    for(i=0;i<10;i++)
        printf("%d ",arr[i]);
    printf("\n");

    return 0;
} 

// printf("hello\n");
    
//     int *arr,i,size=5;
//     arr=(int*)malloc(size*sizeof(int));
//     for(i=0;i<5;i++){
//        // printf("%d\n",i);
        
//         arr[i]=i+1;
//     }
//     // arr[5]=6;
//     // arr[6]=7;
//     // arr[7]=8;
//     // printf("%d\n",arr[7]);
    
//     printf("%d\n",sizeof(arr));
//     printf("%d\n",sizeof(1));
//     for(i=0;i<size;i++)
//         printf("%d ",arr[i]);
//     printf("\n");