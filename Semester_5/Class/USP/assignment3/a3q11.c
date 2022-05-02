/*    Name: Bali Babu Chauhan
      Redg.no.: 19410121182
      Date:2021/12/13
*/
#include <stdio.h>
void f(int *address){
    printf("%p\n",address);
    
}
int main()
{
    int a[3],*pa,i=2;
    pa=a;
    pa++;
    pa=&a[0];
    //a=pa;
    //a++;
    printf("%d  %d\n",pa[i],*(pa+i));
    printf("%p  %p\n",&a[i],(a+i));
    printf("%d  %d\n",a[i],*(a+i));
    printf("%d  %d\n",pa[i],a[i]);
    f(&a[2]);f(a+2);
    printf("working\n");
    return 0;
} 