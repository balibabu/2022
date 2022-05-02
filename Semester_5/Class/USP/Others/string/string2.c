//string details
#include <stdio.h>
#include <string.h>
int main(){
	char str1[20]="hello";
	char str2[20]="Hello";
	printf("%d\n",strcmp(str1,str2));
	char str3[20]="hello";
	char str4[20]="hello";
	printf("%d\n",strcmp(str3,str4));
	char str5[20]="Hello";
	char str6[20]="hello";
	printf("%d\n",strcmp(str5,str6));
	return 0;
}
