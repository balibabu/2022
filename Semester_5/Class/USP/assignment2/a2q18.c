/*    Name: Bali Babu Chauhan
      Redg.no.: 19410121182
      Date:2021/12/10
*/
#include <stdio.h>
void arrange(int *p1, int *p2){
    if(*p1>*p2){
        int temp=*p1;
        *p1=*p2;
        *p2=temp;
    }
}
int main(){
    int a,b,c,d,e,f;
    printf("enter 6 numbers\n");
    scanf("%d%d%d%d%d%d", &a,&b,&c,&d,&e,&f);
    arrange(&a,&b);
    arrange(&b,&c);
    arrange(&c,&d);
    arrange(&d,&e);
    arrange(&e,&f);

    arrange(&a,&b);
    arrange(&b,&c);
    arrange(&c,&d);
    arrange(&d,&e);

    arrange(&a,&b);
    arrange(&b,&c);
    arrange(&c,&d);

    arrange(&a,&b);
    arrange(&b,&c);

    printf("after arranging %d %d %d %d %d %d\n",a,b,c,d,e,f);
    return 0;
} 