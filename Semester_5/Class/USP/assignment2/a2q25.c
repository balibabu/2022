/*    Name: Bali Babu Chauhan
      Redg.no.: 19410121182
      Date:2021/12/10
*/
#include <stdio.h>
#include <string.h>
int main(){
    char sentence1[50];
    char sentence2[50];
    int i = 0;
    printf("Input the string: ");
    scanf("%[^\n]s", sentence1);
    printf("the given sentence is: %s\n",sentence1);
    for (i = 0; i < strlen(sentence1); i++)
    {
        if(sentence1[i]>='a' && sentence1[i]<='z')
            sentence2[i]=sentence1[i]-32;
        else if(sentence1[i]>='A' && sentence1[i]<='Z')
            sentence2[i]=sentence1[i]+32;
        else
            sentence2[i]=sentence1[i];
    }
    sentence2[i]='\0';
    printf("After case Reversal the string is: %s\n",sentence2);
    return 0;
} 

