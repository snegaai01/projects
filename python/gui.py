from tkinter import *

app=Tk()
app.title("ARITHMETIC OPERATIONS")
app.geometry("800x440+300+200")
app.config(bg="pink")


def addition():
    x=int(inputa.get()) 
    y=int(inputbox2.get())
    c=x+y
    labeloutput.config(text=c)


def subtraction():
    x=int(inputa.get()) 
    y=int(inputbox2.get())
    c=x-y
    labeloutput.config(text=c)

def Multiplication():
    x=int(inputa.get()) 
    y=int(inputbox2.get())
    c=x*y
    labeloutput.config(text=c)


def division():
    x=int(inputa.get()) 
    y=int(inputbox2.get())
    c=x/y
    labeloutput.config(text=c)


def modulus():
    x=int(inputa.get()) 
    y=int(inputbox2.get())
    c=x%y
    labeloutput.config(text=c)

def greater():
    x=int(inputbox2.get()) 
    y=int(inputbox2.get())
    c=x>y
    labeloutput.config(text=c)

def Expo():
    x=int(inputa.get()) 
    y=int(inputbox2.get())
    c=x**y
    labeloutput.config(text=c)

def And():
    x=int(inputa.get()) 
    y=int(inputbox2.get())
    c=x&y
    labeloutput.config(text=c)

def OR():
    x=int(inputa.get()) 
    y=int(inputbox2.get())
    c=x|y
    labeloutput.config(text=c)

def equal():
    x=int(inputa.get()) 
    y=int(inputbox2.get())
    c=x==y
    labeloutput.config(text=c)
labelTitle=Label(app, text="Arithmetic operations", fg="red")
labelTitle.grid(row=0, column=2, padx=20)


lbltitle=Label(app,text="Enter value A",font=("cooper"))
lbltitle.grid(row=1, column=1, padx=100 , pady=20)


inputa=Entry(app, width=50)
inputa.grid(row=1, column=2)





lbltitle=Label(app,text="Enter value B",font=("cooper",10))
lbltitle.grid(row=2, column=1, padx=100, pady=20)


inputbox2=Entry(app,width=50)
inputbox2.grid(row=2, column=2)



labeloutput=Label(app,text=" ")
labeloutput.grid(row=3,column=3, pady=20)



btnAdd=Button(app,text="Addition", command=addition)
btnAdd.grid(row=4,column=1)

btnSubtract=Button(app,text="Subtration", command=subtraction)
btnSubtract.grid(row=4,column=2)

btnmulti=Button(app,text="Multiplication", command=Multiplication)
btnmulti.grid(row=5,column=1)

btndiv=Button(app,text="division", command=division)
btndiv.grid(row=5,column=2)

btnmod=Button(app,text="modulus", command=modulus)
btnmod.grid(row=6,column=1)

btngreat=Button(app,text="greatervalue", command=greater)
btngreat.grid(row=6,column=2)

btnexp=Button(app,text="exponentiation", command=Expo)
btnexp.grid(row=7,column=1)

btnand=Button(app,text="And operator", command=And)
btnand.grid(row=7,column=2)

btnor=Button(app,text="Or operator", command=OR)
btnor.grid(row=7,column=3)

btnequal=Button(app,text="Equal", command=equal)
btnequal.grid(row=8,column=1)

  
  

  
app.mainloop()
