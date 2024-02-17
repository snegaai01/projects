from tkinter import *   
 
win = Tk()  
  
win.geometry("400x250")  
  
#creating a label  
username = Label(win, text = "Username").place(x = 30,y = 50)  
  
#creating second label  
password = Label(win, text = "Password").place(x = 30, y = 90)  
    
submitbutton = Button(win, text = "Submit",activebackground = "red", activeforeground = "blue").place(x = 30, y = 120)  
  
e1 = Entry(win,width = 20).place(x = 100, y = 50)  
    
e2 = Entry(win, width = 20).place(x = 100, y = 90)    
  
win.mainloop()  