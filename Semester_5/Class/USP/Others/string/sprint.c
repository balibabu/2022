//string details
#include <stdio.h>
int main(){
	char str[100];
	sprintf(str,"this is sorted in variable %s also including numbers here %d\n","str",45);
	printf("%s",str);
	return 0;
}
