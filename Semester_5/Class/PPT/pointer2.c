#include <stdio.h>
void pointertoConst();
void constPointer();
void dualPointer();
int main()
{
    //pointertoConst();
    //constPointer();
    dualPointer();
    return 0;
} 

void pointertoConst(){
    const int a=10;
    const int b=5;

    const int *p;
    int *k;
    p=&a;
    printf("%d\n", a);
    p=&b;
    printf("%d\n",*p);
    k=&a;
    (*k)++;
    printf("%d\n",*k); 
}

void constPointer(){
    int a=10;

    int *const p=&a;
    
    printf("%d\n", a);
   // p=&b; we can't change the pointer here, p pointer is constant now
    printf("%d\n",*p);
    *p=5; //but we can change the value
    printf("%d\n",*p);
}

void dualPointer(){
    int a=10,b=5;
    int *const p=&a;
    (*p)++;
    printf("%d\n", *p);
    int **k;
    k=&p;
    //++(*k); working
    *k=&b;
    printf("%d\n",**k);
    printf("%d\n", *p);
}