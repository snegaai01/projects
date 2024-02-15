from tkinter import *

win=Tk()

win.title("Arithmatic Operations")
win.geometry("500x500+500+100")
win.state("zoomed")

def addition():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    #print(a+b)
    c=a+b
    labelouptut.config(text=c)

def Subtraction():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    #print(a+b)
    c=a-b
    labelouptut.config(text=c)





labelTitle=Label(win,text="Arithmatic Operations")
labelTitle.grid(row=0,column=20,padx=200, pady=30)

label1msg=Label(win,text="Enter value a :")
label1msg.grid(row=1,column=20)

tbEntrya=Entry(win,width=60)
tbEntrya.grid(row=1,column=25)


label2msg=Label(win,text="Enter value b :")
label2msg.grid(row=2,column=20, pady=20)

tbEntryb=Entry(win,width=60)
tbEntryb.grid(row=2,column=25,pady=20)


labelouptut=Label(win,text="")
labelouptut.grid(row=3,column=30, pady=20)


btnAdd=Button(win,text="Addition", command=addition)
btnAdd.grid(row=4, column=1)

btnSubtract=Button(win,text="Subtraction",command=Subtraction)
btnSubtract.grid(row=4,column=2)



win.mainloop()