//string details
#include <stdio.h>
#include <string.h>
int main(){
	char str1[20];
	char str2[20];
	printf("enter two strings\n");
	scanf("%s",str1);
	//getchar();
	scanf("%s",str2);
	printf("%d\n",strcmp(str1,str2));
	return 0;
}
