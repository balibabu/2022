#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main(){
	pid_t x=fork();
	if(x<0)
		printf("fork failed\n");
	else if(x==0){
		printf("in child\n");
		printf("child pid is %d\n",getpid());
		printf("parent pid is %d\n\n",getppid());
	}else{
		wait(NULL);
		printf("in parent\n");
		printf("child pid is %d\n",getpid());
		printf("parent pid is %d\n",getppid());
	}
	return 0;
}
