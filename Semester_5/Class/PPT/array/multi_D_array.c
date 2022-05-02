#include <stdio.h>

int main(){
    int arr[][3]={{1,2,3},{3,4,5},{6,7,8}};
    // int arr[][2]={1,2,3,4,5,6};
    int *p;
    p=&arr;
    for(int i=0;i<9;i++)
        printf("%d\n",p[i]);

     
    
    return 0;
} 

// int a=9;
// printf("%d\n",a);
//     int a=8;
//     {
//         int a=1;
//         printf("%d\n",a);
//     }
//     printf("%d\n",a);


// a[1][2][3]
// a[0][1][2]+3
// a[1][0][2]+3
// a[1][2][0]+3
// a[0][0][1]
// a[1][0][0]
// a[0][1][0]
// a[0][0][0]