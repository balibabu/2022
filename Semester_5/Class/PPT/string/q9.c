#include <stdio.h>
void occurence(char *str){
    int occ[100],i,j;
    for(i=0;str[i]!='\0';occ[i++]=0);
    for(i=0;str[i]!='\0';i++){
        for(j=0;str[j]!='\0';j++){
            if(str[i]==str[j])
                occ[i]++;
        }
    }
    for(i=0;str[i]!='\0';i++){
        printf("occurences of %c with position %d is %d\n",str[i],i,occ[i]);
    }
}
int main(){
    char str1[100];
    printf("enter a string\n");
    scanf("%[^\n]s",str1);
    occurence(str1);
    return 0;
} 