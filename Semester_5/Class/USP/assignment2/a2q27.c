/*    Name: Bali Babu Chauhan
      Redg.no.: 19410121182
*/
#include <stdio.h>
#include <stdlib.h>
int main(){
    int s1,s2,*m,*n,i,*mn;
    printf("enter size of 1st and 2nd array\n");
    scanf("%d%d",&s1,&s2);
    m=(int*)malloc(s1*sizeof(int));
    n=(int*)malloc(s2*sizeof(int));
    mn=(int*)malloc((s1+s2)*sizeof(int));
    printf("enter value in 1st array\n");
    for(i=0;i<s1;i++)
        scanf("%d", &m[i]);
    printf("enter value in 2nd array\n");
    for(i=0;i<s2;i++)
        scanf("%d", &n[i]);
    int index1=0,index2=0;
    for(i=0;i<(s2+s1);i++){
        if(m[index1]<n[index2] && index1<s1){
            mn[i]=m[index1];
            index1++;
        }else{
            mn[i]=n[index2];
            index2++;
        }      
    }
    printf("first array: ");    
    for(i=0;i<(s1);i++)
        printf("%d ",m[i]);
    printf("\n");
    printf("second array: ");
    for(i=0;i<(s2);i++)
        printf("%d ",n[i]);
    printf("\n");
    printf("merged sorted array: ");
    for(i=0;i<(s1+s2);i++)
        printf("%d ",mn[i]);
    printf("\n");  
    return 0;
} 