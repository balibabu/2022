#include<stdio.h>
#define PI 3.14159
int main(){
	int nEggs,dozen,gross;
	printf("Enter number eggs ");
	scanf("%d",&nEggs);
	gross=nEggs/144;
	nEggs=nEggs%144;
	dozen=nEggs/12;
	nEggs=nEggs%12;
	printf("Your number of eggs is %d gross, %d dozen, and %d\n",gross,dozen,nEggs);
	return 0;
}
