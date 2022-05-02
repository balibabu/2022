/*    Name: Bali Babu Chauhan
      Redg.no.: 19410121182
      Date:2021/12/16
*/
#include <stdio.h>
int main(int argc, char *argv[]){
    printf("total number of command-line arguments passed is %d\n",argc-1);
    for(int i=1;i<argc;i++)
        printf("%s\n",argv[i]);
    return 0;
} 