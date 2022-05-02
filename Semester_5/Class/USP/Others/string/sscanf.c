//string details
#include <stdio.h>
int main(){
	char str[]="your rank is 5 and score 200.50 thank you";
	char str1[30],str2[30],str3[30];
	int num;
	float num2;
	sscanf(str,"%*s %s %*s %d %*s %s %f %*s %*s",str1,&num,str2,&num2);
	printf("%s  %d  %s  %f\n",str1,num,str2,num2);
	return 0;
}
