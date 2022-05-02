#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main(){
	pid_t x=fork();
	printf("child pid is %d\n",getpid());
	printf("parent pid is %d\n",getppid());
	return 0;
}
