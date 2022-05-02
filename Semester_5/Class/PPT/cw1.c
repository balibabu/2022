#include <stdio.h>
#include <string.h>
int main(){
    char alphabets[26];
    char words[26];
    for(int i=0;i<26;alphabets[i++]=0);
    
    printf("enter a word\n");
    scanf("%s", words);
    for(int i=0;i<strlen(words);i++){
        alphabets[words[i]-97]=1;
    }
    // for (int i = 0; i < 26; i++)
    //     printf("%d\n",alphabets[i]);
        
    return 0;
} 