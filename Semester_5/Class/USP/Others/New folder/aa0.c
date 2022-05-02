#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    int i,n;
    pid_t pid;

    if(argc!=2) {
        printf("Usage %s #ofprocesses\n",argv[0]);
        return 1;
    }

    n=atoi(argv[1]);
    
    for(i=1; i<n;i++) {
        if((pid=fork())<=-0) {
            break;
        }
        else {
            wait(NULL);
        }
    }

    printf("i=%d process ID=%ld Parent ID=%ld forkret=%ld\n",i,(long)getpid(),(long)getppid(),(long)pid);
    
    return 0;
}