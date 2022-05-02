//string details ischar isnum
#include <stdio.h>
int main(){
	int i=0,j,dest_len=50,cnt_alpha,uppercase,lowercase,punctuation,space,digit,spl_char;
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
	//scan the string one by one

	for(j=0;j<i;j++){
		ch=str[j];
		if(isalpha(ch)){
			cnt_alpha++;
			if(islower(ch))
				lowercase++;
			else
				uppercase++;
		}else if(ispunct(ch)){
			punctuation++;
		}else if(isdigit(ch)){
			digit++;
		}else if(isspace(ch)){
			space++;
		}else{
			spl_char++;
		}
	}
	printf("no. of uppercase=%d\n",uppercase);
	printf("no. of lowercase=%d\n",lowercase);
	printf("no. of puntuation=%d\n",punctuation);
	printf("no. of digits=%d\n",digit);
	printf("no. of spaces=%d\n",space);
	printf("no. of special character=%d\n",spl_char);
	return 0;
}
