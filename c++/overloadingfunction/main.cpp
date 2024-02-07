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





#include <iostream>
using namespace std;

class Rect{
   private:
   int area;
   public:
   Rect(){
      area = 0;
   }
   Rect(int a, int b){
      area = a * b;
   }
   void display(){
      cout << "The area is: " << area << endl;
   }
};

int main(){
   Rect r1;
   Rect r2(2, 6);
   r1.display();
   r2.display();
}










void addition1(int a , int b){
 cout << endl << " The added value of a and b is :"<< (a+b);
 }
void subtraction (int a , int b)
{

    cout << endl << " The subtracted value of  a and b is :"<< (a-b);
}
void multiplication ( float x , float  y)

{

    cout << endl << " The multiplied value of x and y is:"<< (x*y);
}

int main()
{

    addition1(12,12);
    subtraction(13,16);
    multiplication(12,12);
    return 0;
}





int add(int a , int b)
{

    return(a+b);
}
int add(int a, int b, int c)
{

    return (a+b+c);
}
string add (string  str1, string  str2 ,string str3)
{
    return str1 + str2 + str3;
}

int main()
{

    int sum1= add(10,5);
    int sum2 = add(10,10,23);
    string result = add("  Hello","  Tamil is  a " ,"   scenekaari");
    cout << "sum 1: "<< sum1 << endl;
    cout << "sum2 :"<< sum2<< endl;
    cout << "concatenated string :"<< result << endl;
    return 0;

}

*/




#include <iostream>

using namespace std;
class salaryprint{
private:
    int salary;
public:
    string empname;
    void setsalary(int s){
    salary=s;

    }
int getsalary(){
    return salary;

}
  int getsalaryprint(){
 cout<<salary;

}
void getsalaryprint1(){
cout<<salary;
}
};

int main()
{
 salaryprint sp;
 sp.setsalary(50);
 cout<<sp.getsalary()<<endl;
 sp.getsalaryprint();
 sp.getsalaryprint1();


 if( sp.getsalary()==50){
    cout<<"Its a return type"<<endl;

 }
if( sp.getsalaryprint()==50){
    cout<<"Its a return type"<<endl;
}
    return 0;
}
