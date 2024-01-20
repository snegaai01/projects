#include <iostream>

using namespace std;

int main()
{


int x, y;
    char op;

    cout << "Enter number x: ";
    cin >> x;
    cout << "Enter number y: ";
    cin >> y;


    cout << "Enter arithmetic operator (symbol): ";
    cin >> op;

    switch (op) {
        case '+':
            cout << "output: " << x + y;
            break;
        case '-':
            cout << "output: " << x - y;
            break;
        case '*':
            cout << "output: " << x * y;
            break;
        case '/':
            cout << "output: " << x / y;
            break;


    }
}
