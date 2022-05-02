#include <stdio.h>
#include <stdbool.h>
bool first(){
	printf("first\n");
	return true;
}
bool second(){
	printf("scond\n");
	return false;
}

int main(){
	printf("Hello world\n");
	if(first() || second()){
		printf("in loop\n");
	}
	printf("%d",sizeof('+'));
	return 0;
}

