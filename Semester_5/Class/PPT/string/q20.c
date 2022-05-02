#include <stdio.h>
void shortform(char *str1){ //mine technique
    char str2[100];
    int i,c=0,p1=0;
    for(i=0;str1[i]!='\0';i++){
        if(str1[i]==' '){
            str2[c++]=str1[p1];
            str2[c++]='.';
            for(p1=i+1;str1[p1]==' ';p1++,i++);
        }
    }
    for (i=p1;str1[i]!='\0';i++)
        str2[c++]=str1[i];
    str2[c]='\0';
    printf("%s\n",str2);
}
void short_name(char *fname){ //mam's technique
    char sname[20];
    int i,j,k;
    for(i=0,j=0,k=0;fname[j]!='\0';j++){
        if(fname[j]==' '){
            sname[k++]=fname[i];
            sname[k++]='.';
            i=j+1;
        }
    }
    for(;fname[i]!='\0';i++,k++)
        sname[k]=fname[i];
    sname[k]='\0';
    printf("%s\n",sname);
    
}
int main(){
    char str1[100];
    printf("enter a word\n");
    scanf("%[^\n]s",str1);
    shortform(str1);    //more precise
    short_name(str1);   //less precise
    return 0;
} 