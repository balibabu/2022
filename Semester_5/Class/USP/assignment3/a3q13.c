/*    Name: Bali Babu Chauhan
      Redg.no.: 19410121182
      Date:2021/12/13
*/
#include <stdio.h>
void f(int *address){
    printf("%d\n",*address);
}
int main(){
    int arname[10]={0,1,2,3,4,5};
    f(&arname[2]);
    return 0;
} 