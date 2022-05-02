#include <stdio.h>

int main(){
	int i,j,sum;
	for(i=1;i<=1000;i++){
		sum=1;
		for(j=2;j<i;j++){
			if(i%j==0){
				sum+=j;
			}
		}
		if(sum==i)
			printf("%d ",i);
	}
	printf("\n");
	return 0;
}
