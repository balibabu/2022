/*    Name: Bali Babu Chauhan
	  Redg.no.: 19410121182
	  Date:2021/12/16
*/
#include <stdio.h>
#include <ctype.h>
int main(){
	int i=0,j,dest_len=50,cnt_alpha=0,uppercase=0,lowercase=0,punctuation=0,space=0,digit=0,spl_char=0;
	char ch,str[dest_len];
	printf("enter a string ");
	for(ch=getchar(); ch!='\n' && ch!=EOF && i<dest_len-1; ch=getchar()){
		str[i]=ch;
		i++;
	}
	str[i]='\0';
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
	printf("total no. of alphabets=%d\n",cnt_alpha);	
	printf("no. of uppercase=%d\n",uppercase);
	printf("no. of lowercase=%d\n",lowercase);
	printf("no. of puntuation mark=%d\n",punctuation);
	printf("no. of digits=%d\n",digit);
	printf("no. of spaces=%d\n",space);
	return 0;
}
