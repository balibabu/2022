/*    Name: Bali Babu Chauhan
      Redg.no.: 19410121182
      Date:2021/12/15
*/
#include <stdio.h>
#include <string.h>
void separate_component(char *str){
    char s1[30],s2[30],s3[30];
    int i=0,c=0;
    for(i=0;i<strlen(str);i++)
        if(isalpha(str[i]))
            s1[i]=str[i];
        else
            break;
    s1[i]='\0';
    for(i,c=0;i<strlen(str);i++,c++)
        if(isdigit(str[i]))
            s2[c]=str[i];
        else
            break;
    s2[c]='\0';
    for(i,c=0;i<strlen(str);i++,c++)
        s3[c]=str[i];
    s3[c]='\0';
    printf("Warehouse: %s\n",s1);
    printf("Product: %s\n",s2);
    printf("Qualifiers: %s\n",s3);
}
int main(){
    char str[50];
    printf("enter code from Millies Mail-Order Catalog\n");
    scanf("%s", str);
    separate_component(str);
    return 0;
} 