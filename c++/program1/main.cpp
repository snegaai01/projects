/*#include <iostream>

using namespace std;


class Car {
  public:
    string brand;
    string model;
    int year;
};

int main() {

  Car carObj1;
  carObj1.brand = "BMW";
  carObj1.model = "X5";
  carObj1.year = 1999;


  Car carObj2;
  carObj2.brand = "Ford";
  carObj2.model = "Mustang";
  carObj2.year = 1969;


  cout << carObj1.brand << "\n" << carObj1.model << "\n" << carObj1.year << "\n\n";

  cout << carObj2.brand << "\n" << carObj2.model << "\n" << carObj2.year << "\n";
  return 0;

}


#include <iostream>

using namespace std;

int main()
{

    int a = 10, b = 5;

    cout<<a+b<< endl;
    cout << a - b << endl;
    cout <<a * b << endl;
    cout << a / b << endl;
    cout << a % b << endl;
    return 0;
}
*/
#include <iostream>
using namespace std;

class Room {
   private:
    double length;
    double breadth;

   public:
    // 1. Constructor with no arguments
    Room() {
        length = 6.9;
        breadth = 4.2;
    }

    // 2. Constructor with two arguments
    Room(double l, double b) {
        length = l;
        breadth = b;
    }
    // 3. Constructor with one argument
    Room(double len) {
        length = len;
        breadth = 7.2;
    }

    double calculateArea() {
        return length * breadth;
    }
};

int main() {
    Room room1, room2(8.2, 6.6), room3(8.2);


    cout << "Area of room = " << room1.calculateArea() << endl;


    cout << "Area of room = " << room2.calculateArea() << endl;

    cout << "Area of room = " << room3.calculateArea() << endl;

    return 0;
}
