 #include <iostream>

using namespace std;
/*class salaryprint{
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


*/



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





