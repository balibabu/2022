#include <iostream>
using namespace std;
class test{
    int a,b,sum;
    public:
        void getdata(){
            cin>>a>>b;
        }
        void show(){
            cout<<"\na="<<a<<"\nb="<<b<<"\nSum="<<sum;
        }
        friend void add(test);
};
void add(test t){
    t.sum=t.a+t.b;
}
int main(){
    test tobj;
    tobj.getdata();
    add(tobj);
    tobj.show();
    return 0;
}