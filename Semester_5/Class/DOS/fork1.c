#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main(){
	if(fork()==0)
		printf("A\n");
	else
		printf("B\n");
	return 0;
}
