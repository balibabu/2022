#include <stdio.h>
int compare(char *str1,char *str2){
    for (int i=0;str1[i]!='\0' || str2[i]!='\0';i++){
        if(str1[i]>str2[i])
            return 1;
        else if(str1[i]<str2[i])
            return -1;
    }
    
    
    return 0;
}
int main(){
    char str1[100],str2[100];
    printf("%d\n",(int)('\0'));
    printf("enter 1st string\n");
    scanf("%[^\n]s",str1);
    getchar();
    printf("enter 2nd string\n");
    scanf("%[^\n]s",str2);
    printf("%d\n",compare(str1,str2));
    return 0;
} 