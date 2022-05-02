#include <stdio.h>
#include <string.h>
void frequency(char str[]){
    int freq[26];
    str=strlwr(str);
    for(int i = 0;i<26;freq[i++]=0);
    int n=strlen(str);
    for(int i=0;i<n;freq[str[i++]-'a']++);

    for (int i = 0; i < 26; i++)
        if (freq[i]!=0)
            printf("%c --> %d\n",(char)(i+'a'),freq[i]);
}
int main(){
    char str[30]="HelloWorld";
    int count[30];
    for(int i=0;i<30;count[i++]=0);
    printf("%s\n",str);
    for (int i=0;i<strlen(str);i++){
        for (int j=0;j<strlen(str);j++){
            if(str[i]==str[j])
                count[i]++;
        }
    }

    frequency(str);
    return 0;
} 