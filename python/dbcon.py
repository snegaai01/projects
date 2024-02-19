from tkinter import *

app=Tk()
app.title("STUDENT MARK LIST")
#app.geometry("800x440+300+200")
app.config(bg="pink")
app.state("zoomed")


lbltitle=Label(app,text="NAME").grid(row=1, column=1, padx=100 , pady=20)


inputa=Entry(app, width=50).grid(row=1, column=2)

lbltitle=Label(app,text="TAMIL").grid(row=2, column=1, padx=100 , pady=20)


inputa=Entry(app, width=50).grid(row=2, column=2)



lbltitle=Label(app,text="ENGLISH").grid(row=3, column=1, padx=100 , pady=20)


inputa=Entry(app, width=50).grid(row=3, column=2)


lbltitle=Label(app,text="MATHS").grid(row=4, column=1, padx=100 , pady=20)


inputa=Entry(app, width=50).grid(row=4, column=2)

lbltitle=Label(app,text="SCIENCE").grid(row=5, column=1, padx=100 , pady=20)


inputa=Entry(app, width=50).grid(row=5, column=2)


lbltitle=Label(app,text="SOCIAL").grid(row=6, column=1, padx=100 , pady=20)


inputa=Entry(app, width=50).grid(row=6, column=2)



btnAdd=Button(app,text="INSERT").grid(row=10,column=1)


btnAdd=Button(app,text="UPDATE").grid(row=10,column=2)

btnAdd=Button(app,text="DELETE").grid(row=11,column=1)


btnAdd=Button(app,text="SUBMIT").grid(row=11,column=2)
















app.mainloop()