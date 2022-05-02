#include <iostream>
using namespace std;
template <class T>
class data{
    public:
        data(T x){
            cout<<"\n x= "<<x<<" size in bytes: "<<sizeof(x);

        }
};
int main(){
    data <char> cobj('A');
    data <int> iobj(10);
    data <double> dobj(1.2);
    return 0;
} 
    