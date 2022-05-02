#include<stdio.h>
int main(){
	int arr[10],max,i,sum,min;
	printf("enter 10 numbers\n");
	for(i=0;i<10;i++){
		scanf("%d",&arr[i]);
	}
	max=arr[0];
	min=arr[0];
	sum=arr[0];
	for(i=1;i<10;i++){
		sum+=arr[i];
		if(max<arr[i])
			max=arr[i];
		if(min>arr[i])
			min=arr[i];
	}
	printf("the greatest number is %d\n",max);
	printf("the smallest number is %d\n",min);
	printf("the sum of elements of array is %d\n",sum);
	return 0;
}
