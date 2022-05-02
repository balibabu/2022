//string details
#include <stdio.h>
int main(){
	int i=0,j,dest_len=50;
	char ch,str[dest_len];
	//input starts
	printf("enter a string ");
	for(ch=getchar(); ch!='\n' && ch!=EOF && i<dest_len-1; ch=getchar()){
		str[i]=ch;
		i++;
	}
	str[i]='\0';
	/*clearing residue*/
	while(ch!='\n' && ch!=EOF)
		ch=getchar();
	/*input stop*/
	printf("%s\n",str);
	return 0;
}
