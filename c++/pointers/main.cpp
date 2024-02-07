#include <iostream>

using namespace std;

int main()
{
   int a=10;
   cout << "value of a is:"<< a <<endl;
   cout << "address of a is:"<< &a <<endl;

     int *p=&a;
     cout << "value of p is:"<<p << endl;
     cout << "adress of p is:"<< &p<< endl;
     cout << "value stored in adress of p is:"<< *p<< endl;

     int **q=&p;
     cout << "value of q is:"<<q << endl;
     cout << "adress of q is:"<< &q<< endl;
     cout << "value stored in adress of q is:"<< *q<< endl;


}
