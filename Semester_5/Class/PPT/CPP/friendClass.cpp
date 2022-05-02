#include <iostream>
using namespace std;

class C;
class A{
    int x;
    public:
        void getdata(){
            cin>>x;
        }
        void show(){
            cout<<x;
        }
        friend class C;
};

class B{
    int y;
    public:
        void getdata(){
        cin>>y;
        }
        void show(){
            cout<<y;
        }
        friend class C;
};

class C{
    int add_res;
    int sub_res;
    int mult_res;
    int div_res;
    // A a;
    // B b;
    public:
        void add(A a,B b){
            add_res=a.x+b.y;
        }
        void subt(A a,B b){
            sub_res=a.x-b.y;
        }
};