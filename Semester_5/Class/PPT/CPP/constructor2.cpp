#include <iostream>
using namespace std;

class rectangle{
    int len;
    int br;
  public:
    rectangle(int l=0,int b=0){
        len=l;
        br=b;
    }
    rectangle(rectangle &r){
        len=r.len;
        br=r.br;
    }
    void show(){
        cout<<"\nLength:"<<len
        <<" Breadth:"<<br;
    }
    ~rectangle(){
        len=br=0;
    }
};

int main(){
    rectangle r1;           //default constructor
    r1.show();              //length:0 breadth:0
    rectangle r2(10,7);     //parameterized constructor         
    r2.show();              //length:10 breadth:7
    rectangle r3(r2);       //copy constructor
    r3.show();              //length:10 breadth:7
    rectangle r4;           //copy constructor
    r4.show();              //length:0 breadth:0
    r4=r2;                  //assigns the respective properties of r2 to r4
    r4.show();              //length:10 breadth:7
    
    return 0;
}