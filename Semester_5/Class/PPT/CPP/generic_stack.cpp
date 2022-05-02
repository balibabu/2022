#include <iostream>
using namespace std;
#define MAX 10
template <class T>
class Stack{
    T arr[MAX];
    int top;
  public:
    Stack(){
        top=-1;
    }
    void push(T n){
        if(top==MAX-1){
            cout<<"\nStack is full";
            return;
        }
        arr[++top]=n;
    }
    void pop(){
        if(top==-1){
            cout<<"\nStack is empty";
            return;
        }
        cout<<arr[top--];
    }
};
int main(){
    Stack<int> s;
    s.pop();
    return 0;
} 