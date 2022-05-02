#include <iostream>
using namespace std;
int main(){
    int x,y;
    cout<<"enter the numerator and denominator respectively ";
    cin>>x>>y;
    try{
        if(y==0)
            throw (y);
        int res=x/y;
        cout<<"\n"<<res;
    }catch(int j){
        cout<<"\nEnter a non-zero denominator";
    }
    return 0;
}