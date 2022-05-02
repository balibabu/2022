#include <stdio.h>
#include <string.h>
void encrypt(char *str1,int key){
    int l=strlen(str1),arr[100],i;
    if (key>l){
        arr[0]=l;
        arr[1]=key;
    }else{
        arr[0]=key;
        arr[1]=l;
    }
    for(i=2;i<l;i++)
        arr[i]=(key+l+arr[i-2]+arr[i-1])%10;
    for(i=0;str1[i]!='\0';i++)
        str1[i]+=arr[l-i];
}
void decrypt(char *str1,int key){
    int l=strlen(str1),arr[100],i;
    if (key>l){
        arr[0]=l;
        arr[1]=key;
    }else{
        arr[0]=key;
        arr[1]=l;
    }
    for(i=2;i<l;i++)
        arr[i]=(key+l+arr[i-2]+arr[i-1])%10;
    for(i=0;str1[i]!='\0';i++)
        str1[i]-=arr[l-i];
}
int main(){
    char str1[100];
    int key;
    printf("enter a string\n");
    scanf("%[^\n]s",str1);
    printf("enter encryption key\n");
    scanf("%d", &key);
    encrypt(str1,key);
    printf("encrypted text is:\n%s\n",str1);
    printf("enter decryption key\n");
    scanf("%d", &key);
    decrypt(str1,key);
    printf("decrypted text is:\n%s\n",str1);
    return 0;
} 