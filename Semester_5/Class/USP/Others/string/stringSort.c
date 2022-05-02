//string details
#include <stdio.h>
#include <string.h>
int main(){
	char strArray[5][10];
	char strTemp[10];
	int i,j;
	for(i=0;i<5;i++){
		printf("Enter a name\n");
		scanf("%s",strArray[i]);
	}
	printf("\nThe entered strings are :\n");
	for(i=0;i<5;i++){
		printf("%s\n",strArray[i]);
	}
	printf("\n\n");
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			if(strcmp(strArray[j], strArray[j+1])>0){
				strcpy(strTemp,strArray[j]);
				strcpy(strArray[j],strArray[j+1]);
				strcpy(strArray[j+1],strTemp);
			}
		}
	}
	printf("The sorted strings are :\n");
	for(i=0;i<5;i++){
		printf("%s\n",strArray[i]);
	}

	return 0;
}
