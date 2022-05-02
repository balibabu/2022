#include <iostream>
using namespace std;
template <typename T>
T add(T a,T b){
    return a+b;
}
int main(){
    int x=10,y=20;
    float fx=2.5,fy=3.4;
    int r=add<int>(x,y);
    float fr=add<float>(fx,fy);
    cout<<"\n sum="<<r;
    cout<<"\n sum="<<fr;
    return 0;
} 