/*#include <iostream>

using namespace std;

class Animal
 {
   public:

 void eat()
 {
    cout<<"Eating..."<<endl;
 }

   };

   class Dog: public Animal

   {
       public:

     void bark()
     {
    cout<<"Barking...";
     }
   };

int main(void)
{
    Dog d1;
    d1.eat();
    d1.bark();
    return 0;



}




    #include <iostream>

using namespace std;


class Shape

{
   public:
      void setWidth(int w) {
         width = w;
      }
      void setHeight(int h) {
         height = h;
      }

   protected:
      int width;
      int height;
};


class PaintCost
{
   public:
      int getCost(int area)
      {
         return area * 70;
      }
};


class Rectangle: public Shape, public PaintCost {
   public:
      int getArea()
       {

         return (width * height);
      }
};

int main(void)
 {
   Rectangle Rect;
   int area;

   rect.setWidth(5);
   rect.setHeight(7);

   area = Rect.getArea();


   cout << "Total area: " << Rect.getArea() << endl;


   cout << "Total paint cost: $" << Rect.getCost(area) << endl;

   return 0;
}





#include <iostream>
using namespace std;
class Base
{
public:
int base_value;
void base_input()
{
cout<<"Enter the integer value of base class: ";

cin>>base_value;
}

};
class Derived : public Base
{

int derived_value;
public:
void derived_input()

{
cout<<"Enter the integer value of derived class: ";

cin>>derived_value;
}
void sum()
{

cout << "The sum of the two integer values is: " << base_value + derived_value<<endl;
}

};

int main()
{

cout<<"Welcome to scenekaari (tamil) tutorials!"<<endl<<endl;

Derived d;

d.base_input();
d.derived_input();
d.sum();
return 0;
}




#include <iostream>
using namespace std;
class Base
{
public:
int base_value;
void base_input()
{
cout<<"Enter the first value: ";
cin>>base_value;
}
};
class Derived : public Base
{

int derived_value;
public:
void derived_input()
{
cout<<"Enter the second  value(derived class): ";
cin>>derived_value;
}
void sum()
{
cout << "The Addded value of first and second  is: "<< base_value + derived_value<<endl;
}
};
int main()
{
cout<<"Addition of two values using inheritance "<<endl<<endl;
Derived d;
d.base_input();
d.derived_input();
d.sum();
return 0;
}




*/

#include <iostream>
using namespace std;
class A
{
public:
int i;
void geti()
{
cout<<"Enter the number: "<<endl;
cin>>i;
}
};

class B
{
public:
int j;
void evaluate()
{
if(j%2==0)
{
cout<<"Entered number is even."<<endl;
}
else
{
cout<<"Entered number is odd."<<endl;
}
}
};

class C : public A, public B
{
public:
void display()
{
cout<<"Multiple inheritance successfully executed."<<endl;
}
};

int main()
{
C obj;
obj.geti();
obj. j=obj.i;
obj.evaluate();
obj.display();
return 0;
}
