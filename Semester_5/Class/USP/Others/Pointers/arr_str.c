#include <stdio.h>
#include <string.h>
void length();


int main(){
	length();
	return 0;
}



void length(){
	int i=0;
	char str[20]="hell word";
	char *ptr="Hello World";
	printf("str=%s and ptr=%s\n",str,ptr);
	
	//strcpy(str,ptr);
	ptr=str; //binding str and ptr
	printf("After binding str=%s and ptr=%s\n",str,ptr);

	printf("length of str is %d\n",(int)strlen(str));
	printf("length of ptr is %d\n",(int)strlen(ptr));
	
	/*for(i=0;i<strlen(ptr);ptr++){
		printf("ptr[%d] is %c\n",i,ptr[i]);
		//printf("length of ptr is %d\n",strlen(ptr));
	}
	*/
	for(i=0;i<strlen(ptr);i++){
		printf("ptr[%d] is %c\n",i,ptr[i]);
		//printf("length of ptr is %d\n",strlen(ptr));
	}
}
