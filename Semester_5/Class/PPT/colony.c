#include<stdio.h>
void colony(int[],int);
int main(){
    int arr[]={1,0,0,0,0,1,0,0};
    int l=8;
    colony(arr,l);
    for(int i=0;i<l;i++){
        printf("%d ",arr[i]);
    }
    printf("\n");
    return 0;
}

void colony(int arr[],int d){
    int l=sizeof(arr)/sizeof(0);
    int temp[l],i=0;
    temp[0]=0^arr[1];
    for(i=1;i<l-1;i++){
        temp[i]=arr[i-1]^arr[i+1];
    }
    temp[l-1]=0^arr[l-1];
    for(int i=0;i<l;i++){
        arr[i]=temp[i];
    }
    
}