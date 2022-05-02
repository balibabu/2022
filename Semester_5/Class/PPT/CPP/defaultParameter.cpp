#include <iostream>
using namespace std;
int sum(int a,int b=7);
int main(){
    cout<<sum(4)<<endl;
    cout<<sum(1,2);
    return 0;
} 
int sum(int a,int b){
    return a+b;
}