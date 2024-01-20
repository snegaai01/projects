
#include<iostream>
using namespace std;

class Add {

public:
    int addition;
    int subtraction(int x, int y) {
        return x + y;
    }
};

int main() {

    int x, y, s;

    cout << "Enter two numbers:";
    cin >> x >> y;

    Add obj;
    s = obj.addition(x, y);
    s = obj.subtraction(x,y);

    cout << "Sum of two numbers:" << s;
    cout<< "subtraction  of two numbers:"<< s;

    return 0;
}
C++
Output:
