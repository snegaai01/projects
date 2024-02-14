from tkinter import *

app=Tk()
app.title("WELCOME TO GUI")
app.geometry("600x300+500+200")
app.config(bg="pink")
lbltitle=Label(app,text="ADDITION")
lbltitle.grid(row=2, column=1, padx=60 , pady=60)


inputbox1=Entry(app,width=20)
inputbox1.grid(row=2, column=2)

lbltitle=Label(app,text="SUBTRACTION")
lbltitle.grid(row=3, column=1, padx=50, pady=20)
inputbox2=Entry(app,width=20)
inputbox2.grid(row=3, column=2)


app.mainloop()
