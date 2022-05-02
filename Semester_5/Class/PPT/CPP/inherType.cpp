#include <iostream>
using namespace std;

class A{
    int x;
  public:
    void getA(){
        cout<<"enter value in x ";
        cin>>x;
    }
    void showA(){
        cout<<"in A, x="<<x<<endl;
    }
};

class B: private A{
    int y;
  public:
    void getB(){
        cout<<"enter value in y ";
        cin>>y;
    }
    void showA(){
        cout<<"in B, x="<<y<<endl;
    }
};

class C: private B{
     int z;
  public:
    void getC(){
        cout<<"enter value in z ";
        cin>>z;
    }
    void showC(){
        cout<<"in C, x="<<z<<endl;
    }
};
int main(){
    C obj;
    // obj.getA();  can't access members of A because B import A privately
    // obj.getB();  members of B is accesible inside C class not outside
    obj.getC();
    obj.showC();
    return 0;
} 