#include <iostream>

using namespace std;

int main()


{
    string name;
/*   cout << "Enter your name:" << endl;
    cin >> name;
    cout << name << endl;
    fflush(stdin);
    cout <<  "Enter your name:" << endl;
    getline(cin ,name);
    cout << name << endl;
    return 0;
}


{
    int n;
    string str;
    cout << "Enter the number:"<< endl;
    cin >> n;
    fflush(stdin);
    fflush(stdin);
    getline(cin, str);
    cout << n << endl << str << endl;
}




string firstname;
string lastname;
cin >> firstname >> lastname;
cout << firstname + " " + lastname << endl;
string fullname = firstname.append(lastname);
cout << fullname << endl;
lastname.push_back('t');

cout << lastname<< endl;
firstname.push_back('sr');
cout << firstname;

/*
string fullname;
cout << "Enter your name:" << endl;
cin >> fullname;
cout << "Length of a string is:";
cout << fullname.length() << endl;
cout << "Size of the string is:";
cout << fullname.size();
*/
fflush(stdin);
string fullname;
cout << "Enter your name:";
cin >> fullname;
fullname.insert(2, " am ");
cout << fullname;
return 0;
}
