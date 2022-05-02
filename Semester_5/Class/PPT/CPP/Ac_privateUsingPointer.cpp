#include <iostream>
using namespace std;
class test{
    int a;
    float b;
  public:
    test(int x=0,float y=0.0){
        a=x;
        b=y;
    }
    void display(){
        cout<<"\na="<<a;
        cout<<"\nb="<<b;
    }
};
int main(){
    test t(10,20.9);
    int ival=15;
    float fval=22.19;

    int *ptr;
    float *fptr;

    t.display();

    ptr=(int*)&t;
    //at &t is of test type and ptr can hold the address of
    //an integer, it must be typecasted to int*

    *ptr=ival;
    *ptr++;

    fptr=(float*)ptr;
    //ptr is an integer pointer where as fptr is a pointer
    //to float. so typecasting to float * is done
    *fptr=fval;

    t.display();    
    return 0;
} 