#include <stdio.h>
#define SQR(a) a*a //to solve this we use (a)*(a)
//#define SQR(a) (a)*(a)
int sqr(int a){
    return a*a;
}

int main(){
    printf("sqr=%d\n",sqr(5+5)); // this takes as 10*10=100
    printf("SQR=%d\n",SQR(5+5));//macro literally takes as 5+5*5+5=35
    return 0;
} 