#include <stdio.h>
#include <math.h>
int main(){
	int n,tmp,k;
	scanf("%d",&n);
	for(int i=1;i*i<=n;i++){
		if(n%i==0){
			tmp=n/i;
			tmp==i? printf("%d ",i) : printf("%d %d ",i,tmp);
		}
	}
	return 0;
}
