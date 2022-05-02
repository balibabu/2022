#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
int main(){
	int *x=0;
	/*pid_t a=fork();
	pid_t b=fork();
	pid_t c=fork();
	printf("%d\n",a&b&c);*/
	(*x)++;
	printf("%d\n",*x);
	return 0;
}

