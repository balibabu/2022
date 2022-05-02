//creating custom string
#include <stdio.h>
#include <string.h>
int main(){
	int ch,i=0,size=50;
	char str[size];
	while((ch=getchar())!='\n' && i<size-1){
		str[i++]=ch;
	}
	str[i]='\0';
	printf("%s\n",str);
	return 0;
}
