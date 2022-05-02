#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main(){
	int x=5;
	if(fork()==0){
		x+=20;
		printf("%d\n",x);
	}else{
		x+=10;
		printf("%d\n",x);
	}
	return 0;
}
