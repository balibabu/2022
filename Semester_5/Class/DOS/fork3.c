#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main(){
	int x=5;
	if(fork()==0){
		printf("%d\n",++x);
	}else{
		printf("%d\n",--x);
	}
	return 0;
}
