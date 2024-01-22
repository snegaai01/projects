#include <iostream>
using namespace std;
/*
class cons
{

public:
    float area;


    cons()
    {
        area = 0;
    }


    cons(int a, int b)
    {
        area = a * b;
    }

    void output1()
    {
        cout<< area<< endl;
    }
};

int main()
{
    cons a;
    cons b(20.3, 20.7);

    a.output1();
    b.output1();
    return 1;
}
 */



void add(int a, int b)

{

cout<<"addition of a and b is: = " << (a + b);

}
void sub( float a, float b)
{

    cout<<"subtraction value of a and b is : = "<<(a-b);
}

void add(double a, double b)

{
cout << endl << "addition value of a and b is: = " << (a + b);
}

void multiply(int x, int y)
{

    cout<< endl<< "multiplied value of x and y is:="<<(x*y);
}
 void divide(float x, float y)
 {

     cout<< endl<< "Divided value of x and y is:"<<(x/y);
 }

int main()
{
add(10, 2);
sub(29.3,40.4);
add(5.3, 6.7);
multiply(3,7);
divide(40.5,80.5);
return 0;
}
