/*    Name: Bali Babu Chauhan
      Redg.no.: 19410121182
      Date:2021/12/16
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(){
    int n,i,j;
    char arr[30][30],temp[30];
    printf("Input number of strings :");
    scanf("%d", &n);
    for(i=0;i<n;i++)
        scanf("%s", arr[i]);
    for(i=0;i<n-1;i++){
        for(j=0;j<n-i-1;j++){
            if(strcmp(arr[j],arr[j+1])>0){
                strcpy(temp,arr[j]);
                strcpy(arr[j],arr[j+1]);
                strcpy(arr[j+1],temp);
            }
        }
    }
    for(i=0;i<n;i++)
        printf("%s\n",arr[i]);    
    return 0;
} 