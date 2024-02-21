from tkinter import *
import mysql.connector
win=Tk()

win.title("Insert into MYSQL DB Demo")
win.geometry("500x500")

class framewindows:
    def __init__(self) :
        frametop=Frame(win,bg="violet",width=500,height=500, padx=30,pady=30)
        frametop.pack(side = TOP)
        btninsert=Button(frametop,text="INSERT",command=self.frameLeft).pack(padx=10,pady=10)
        btnupdate=Button(frametop,text="UPDATE",command=self.frameright).pack(padx=10,pady=10)
        btndelete=Button(frametop,text="DELETE",command=self.framebottom).pack(padx=10,pady=10)
   
   
    def frameLeft(self):
        newW=Tk()
        newW.title("Insert into MYSQL DB Demo")

        
        frameleft=Frame(newW,bg="deeppink",width=500,height=500, padx=30,pady=30)
        frameleft.pack(side = LEFT)


        lbl_Title_of_oeration=Label(frameleft,text="Insert into MYSQL DB Demo")
        lbl_Title_of_oeration.grid(row=0, columnspan=5)

        lblname=Label(frameleft,text="name")
        lblname.grid(row=2, column=1,padx=30,pady=10)

        invalue1=Entry(frameleft,width=30)
        invalue1.grid(row=2, column=3)

        

        lblTamil=Label(frameleft,text="age")
        lblTamil.grid(row=3, column=1,padx=30,pady=10)

        invalue2=Entry(frameleft,width=30)
        invalue2.grid(row=3, column=3)

        submit=Button(frameleft,text="INSERT")
        submit.grid(row=4, column=3)




    def frameright(self):

        newW=Tk()
        newW.title("Update into MYSQL DB Demo")

        frameright=Frame(newW,bg="cyan",width=500,height=500,padx=30,pady=30)
        frameright.pack(side = RIGHT)

        lbl_Title_of_oeration=Label(frameright,text="Update into MYSQL DB Demo")
        lbl_Title_of_oeration.grid(row=0, columnspan=5)

        lblname=Label(frameright,text="REG.NO")
        lblname.grid(row=2, column=1,padx=30,pady=10)

        invalue1=Entry(frameright,width=30)
        invalue1.grid(row=2, column=3)


        lblTamil=Label(frameright,text="NAME")
        lblTamil.grid(row=3, column=1,padx=30,pady=10)

        invalue2=Entry(frameright,width=30)
        invalue2.grid(row=3, column=3)

        update=Button(frameright,text="UPDATE")
        update.grid(row=4, column=3)



    def framebottom(self):

        newW=Tk()
        newW.title("Update into MYSQL DB Demo")

        framebottom=Frame(newW,bg="pink",width=300,height=300,padx=30,pady=30)
        framebottom.pack(side= BOTTOM)

        lbl_Title_of_oeration=Label(framebottom,text="delete into MYSQL DB Demo")
        lbl_Title_of_oeration.grid(row=0, columnspan=5)

        lblname=Label(framebottom,text="REG-NO")
        lblname.grid(row=2, column=1,padx=30,pady=10)

        invalue1=Entry(framebottom,width=30)
        invalue1.grid(row=2, column=3)


        lblTamil=Label(framebottom,text="NAME")
        lblTamil.grid(row=3, column=1,padx=30,pady=10)

        invalue2=Entry(framebottom,width=30)
        invalue2.grid(row=3, column=3)

        delete=Button(framebottom,text="DELETE")
        delete.grid(row=4, column=3)


run=framewindows() 
win.mainloop()    
