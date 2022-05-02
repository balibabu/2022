/*    Name: Bali Babu Chauhan
	  Redg.no.: 19410121182
	  Date:2021/12/10
*/
#include <stdio.h>
int main(){
        int **Tptr,*ptr,Ivar=454;
        ptr=&Ivar;
        Tptr=&ptr;
        printf("%d\n",**Tptr);   
        return 0;
} 