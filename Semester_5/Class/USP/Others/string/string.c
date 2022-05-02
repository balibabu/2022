#include <stdio.h>
#include <string.h>
int main(){
	//char str[5];
	//scanf("%[^\n]s",str);  //custom scanf
	//printf("str=%s\n",str);
	//char str2[30];
	//strcpy(str2,str);
	//printf("str2=%s\n",str2);
	//char str3[30];
	//strncpy(str3,str,3);
	//printf("str3=%s\n",str3);
	char str[5]="bali";
	printf("str=%s\n",str);
	strcat(str,"hello world");
	printf("str=%s\n",str);
	return 0;
}
