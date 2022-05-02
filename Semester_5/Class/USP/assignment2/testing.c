#include <stdio.h>
//custom scanf or custom input string input string
int main()
{
    char str[30],str1[30],str2[30],str3[30],str4[30];
    // scanf("%[^\n]s",str);  //accepts all except line break
    // printf("%s\n",str);

    // scanf("%[a-zA-Z]s",str1);  //accepts only small and capital alphabets
    // printf("%s\n",str1);

    // scanf("%[0-9]s",str2);       //accepts only number from 0 to 9
    // printf("%s\n",str2);

    scanf("%[^0]s",str3);       //accepts everything except 0
    printf("%s\n",str3);

    return 0;
} 