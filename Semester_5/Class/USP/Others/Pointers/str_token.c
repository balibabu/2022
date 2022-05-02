#include <stdio.h>
#include <string.h>
int main(){
	char str[]="This is, a sample, string";
	char *pch;
	char ns[10][20];
	int i=0,j;
	printf("string to be splitted into tokens is \"%s\"\n",str);
	pch=strtok(str," ,");
	while(pch!=NULL){
		//printf("%s\n",pch);
		strcpy(ns[i++],pch);
		pch=strtok(NULL," ,");
	}
	for(j=0;j<i;j++){
		printf("%s\n",ns[j]);
	}
	return 0;
}
