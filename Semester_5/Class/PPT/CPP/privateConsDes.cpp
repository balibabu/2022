#include <iostream>
/*
One is accesible to only 'public' properties of a class. Thus if the constructor and destructor are 
declared as 'private' it won't be possible to create an object through an implicit call to constructor 
rather the constructor and destructor need to be called explicitly.
*/
using namespace std;

class A{
  private:
    int x;
    A(){
        x=15;
        cout<<"\nIn constructor";
    }
    ~A(){
        x=0;
        cout<<"\nIn destructor";
    }
  public:
    void show(){
        A(); //calls constructor
        cout<<"\nx="<<x;
        // this->A::~A(); //calls destructor
    }
};

int main(){
    // A a; //cannot be executed as it has a private constructor
    A *a;
    a->show();
    return 0;
} 