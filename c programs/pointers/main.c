#include <stdio.h>
#include <stdlib.h>

int main()
{
   int a=10;
   printf("value of a is %d:\n",a);
   printf("Adress of a is %d\n\n", &a);

   printf("size of integers is :%d\n", sizeof(int));
   printf("size of vale a is:%d\n\n", sizeof(a));

   int *p=&a;
   printf("value of p is:%d\n",p);
   printf("adress of p is:%d\n",&p);
   printf("value stored in address of p is:%d\n\n",*p);

   int **q=&p;
   printf("value of q is:%d\n",q);
   printf("adress of q is:%d\n",&q);
   printf("value stored in address of q is:%d\n\n",*q);

   int ***r=&q;
   printf("value of r is:%d\n",r);
   printf("adress of r is:%d\n",&r);
   printf("value stored in address of r is:%d\n\n",*r);


   float b=1.2;
   printf("value of a is %f:\n",b);
   printf("Adress of a is %p\n\n", &b);


  char ch='y';
  printf("value of the character is:%c",y);

}
