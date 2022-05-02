#include <stdio.h>
#include <stdlib.h>
int main(int argc, char* argv[]){
	int size,i;
	
	printf("Program name is %s\n",argv[0]);
	printf("Number of Arguments passed: %d\n",argc);
	if(argc<2){
		printf("No Extra Command Line Argument Passed Other than Program Name\n");
	}else{
		printf("\nFollowing are the CmdLine Args\n");
		for(i=0;i<argc;i++)
			printf("argv[%d]=%s\n",i,argv[i]);
	}
	return 0;
}
