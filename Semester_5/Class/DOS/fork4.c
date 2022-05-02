#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main(){
	pid_t a=fork();
	pid_t b=fork();
	pid_t c=fork();
	printf("child=%d\n",getpid());
	printf("parent=%d\n",getppid());
	return 0;
}
