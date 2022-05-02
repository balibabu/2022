#include <stdio.h>
#include <string.h>
void removeDuplicates(char *str1,char *str2){
    int i,j,s2=0,c;
    for(i=0;str1[i]!='\0';i++){
        c=0;
        for(j=0;j<s2;j++){
            if(str1[i]==str2[j])
                c++;
        }
        if(c==0)
            str2[s2++]=str1[i];
    }
    str2[s2]='\0';
}
int main(){
    char str1[100],str2[100];
    printf("enter a string\n");
    scanf("%[^\n]s",str1);
    removeDuplicates(str1,str2);
    printf("%s\n",str2);
    
    return 0;
}  