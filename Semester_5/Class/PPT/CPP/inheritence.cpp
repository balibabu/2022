#include <iostream>
using namespace std;
class Line
{
  private:
	int len;

  public:
	void accept()
	{
		cout << "\nEnter length ";
		cin >> len;
	}
	void display()
	{
		cout << "\nlength=" << len;
	}
};
class Rectangle : public Line
{
  private:
	int br;

  public:
	void accept()
	{
		Line::accept();
		cout << "\nEnter breadth ";
		cin >> br;
	}
	void display()
	{
		Line::display();
		cout << "\nBreadth=" << br;
	}
};
int main()
{
	Rectangle r;
	r.accept();
	r.display();
	return 0;
}