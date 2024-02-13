class google:
   def func1(self):
        print("Google! google! google!")
class drive:
   def func2(self):
        print("google drive ! google drive !")
class gmail(google , drive):
    def func3(self):
        print("GOOGLE! DRIVE! ")
 
ob = gmail()
ob.func1()
ob.func2()
ob.func3()



class A:
    def __init__(self, a):
        print("first class A")
        self.a = a

class B:
    def __init__(self, b):
        print("second class B")
        self.b = b

class C(A, B):
    def __init__(self, c):


        print("Third class C")
        super().__init__

        
        self.c = c * 5

c = C(6)
print(c.a, c.b, c.c)
