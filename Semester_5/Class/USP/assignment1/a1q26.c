#include <stdio.h>
void question_a();
void question_b();
void question_c();
int main()
{
    question_c();
    return 0;
} 

void question_a(){
    int item,product;
    printf("enter number of item\n");
    scanf("%d",&item);
    printf("enter the value of product\n");
    scanf("%d",&product);
    if(item!=0)
        product*=item;
    printf("the value of product is %d\n",product);
}

void question_b(){
    int x,y;
    printf("enter value of x and y\n");
    scanf("%d%d",&x,&y);
    if(x-y<0)
        y-=x;
    else
        y=x-y;
    printf("x=%d,y=%d\n",x,y);  
}
void question_c(){
    int x,zero_count=0,minus_sum=0,plus_sum=0;
    printf("enter the value of x\n");
    scanf("%d",&x);
    if(x==0)
        zero_count++;
    else if(x<0)
        minus_sum+=x;
    else
        plus_sum+=x;
    printf("zero count=%d\n",zero_count);
    printf("minus sum=%d\n",minus_sum);
    printf("plus sum=%d\n",plus_sum);
}