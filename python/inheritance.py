
class grandparents:




    def __init__(self,grandpaname, grandmaname, familyname) :
        self.grandfathername=grandpaname
        self.grandmothername=grandmaname
        self.familyname=familyname

    def welcome(self):
        print("Welcome to ", self.familyname, " wishes from ", self.grandfathername, " and ", self.grandmothername )
    
        

# x=grandparents("Tamil","srinidhi","punitha")
# x.welcome()
        



class mkazhagiri(grandparents):
     pass

x=mkazhagiri("Tamil","srinidhi","mental families")
x.welcome()

     



class mkazhagiri(grandparents):
    def __init__(self, grandpaname, grandmaname, familyname, fathername,mothername):
        self.fathername=fathername
        self.mothername=mothername
        super().__init__(grandpaname, grandmaname, familyname)

    def thanks(self):
        print("Hi..! Granpa ", self.grandfathername ,"and Grandma ", self.grandmothername , " We ", self.fathername, "and ", self.mothername, " thank you for warm welcome to our " , self.familyname, "family")


# x=mkazhagiri("kalaingar","Dhayalu ammal","DMK")
# x.welcome()

x=mkazhagiri("Tamil","srinidhi","Mental ", "punitha", "snega")
x.welcome()
x.thanks()



class sonname(grandparents):
    def __init__(self, grandpaname, grandmaname, familyname, fathername,mothername,sonname,son2name):
        self.fathername=fathername
        self.mothername=mothername
        self.sonname=sonname
        self.son2name=son2name
        super().__init__(grandpaname, grandmaname, familyname)

    def thank(self):
        print("Hi..! Granpa ", self.grandfathername ,"and Grandma ", self.grandmothername , " We ", self.fathername, "and ", self.mothername, " thank you for warm welcome to our " , self.familyname, "family",self.sonname, "srinidhi",self.son2name, "tamil")


x=sonname("Tamil","srinidhi","Mental ", "punitha", "snega","sri","Tamil selvi")

x.thank()

