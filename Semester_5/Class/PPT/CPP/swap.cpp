#include <iostream>
using namespace std;
void swap1(int *a,int *b){
    int temp=*a;
    *a=*b;
    *b=temp;
}
void swap2(int &a,int &b){
    int temp=a;
    a=b;
    b=temp;
}
int main(){
    int a=9,b=2;
    // swap1(&a,&b);
    swap2(a,b);
    cout<<a<<","<<b;
    return 0;
} 
