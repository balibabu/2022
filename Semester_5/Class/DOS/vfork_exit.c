#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main(){
	pid_t x=vfork();
	if(x<0)
		printf("vfork failed\n");
	else if(x==0){
		printf("in child\n");
		printf("child pid is %d\n",getpid());
		printf("parent pid is %d\n\n",getppid());
		_exit(0); //denote child successfully completed
	}else{
		printf("in parent\n");
		printf("child pid is %d\n",getpid());
		printf("parent pid is %d\n",getppid());
	}
	return 0;
}
