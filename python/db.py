from tkinter import *
import mysql.connector

app=Tk()
app.title("STUDENT MARK LIST")
#app.geometry("800x440+300+200")
app.config(bg="pink")
app.state("zoomed")



def MyDBConnection():
    con=mysql.connector.connect(
    host="192.168.1.240",
    user="AIBATCH01",
    password="AI@123",
    database="ai_snega"
    )
    return con

# print(con)
# print("connected to database at ",con)        

    
def insertvalues():
    NAME=inputa.get()
    TAMIL=inputb.get()
    ENGLISH=inputc.get()
    MATHS=inputd.get()
    SCIENCE=inpute.get()
    SOCIAL=inputf.get()
    e_con=MyDBConnection()
    result=e_con.cursor()
    statement="insert into std_marks(NAME,TAMIL,ENGLISH,MATHS,SCIENCE,SOCIAL)values(%s,%s,%s,%s,%s,%s);"
    valuepass=(NAME,TAMIL,ENGLISH,MATHS,SCIENCE,SOCIAL)
    result.execute(statement,valuepass)
    e_con.commit()
    print(result.rowcount,"row inserted")



def updatevalues():
    MATHS=inputd.get()
    TAMIL=inputb.get()
    

    e_con=MyDBConnection()
    result=e_con.cursor()

    statement="update std_marks set MATHS = (%s) where sno = (%s);"
    valuepass=(MATHS,TAMIL)
    result.execute(statement,valuepass)
    e_con.commit()

    print(result.rowcount, " row updated")
 
def deletevalues():
    NAME=inputa.get()

    e_con=MyDBConnection()
    result=e_con.cursor()

    statement="delete from std_marks where sno = (%s);"
    valuepass=(NAME,)
    result.execute(statement,valuepass)
    e_con.commit()

    print(result.rowcount, " row deleted")  











lbltitle=Label(app,text="NAME")
lbltitle.grid(row=1, column=1, padx=100 , pady=20)


inputa=Entry(app, width=50)
inputa.grid(row=1, column=2)

lbltitle=Label(app,text="TAMIL").grid(row=2, column=1, padx=100 , pady=20)


inputb=Entry(app, width=50)
inputb.grid(row=2, column=2)



lbltitle=Label(app,text="ENGLISH").grid(row=3, column=1, padx=100 , pady=20)


inputc=Entry(app, width=50)
inputc.grid(row=3, column=2)


lbltitle=Label(app,text="MATHS").grid(row=4, column=1, padx=100 , pady=20)


inputd=Entry(app, width=50)
inputd.grid(row=4, column=2)

lbltitle=Label(app,text="SCIENCE").grid(row=5, column=1, padx=100 , pady=20)


inpute=Entry(app, width=50)
inpute.grid(row=5, column=2)


lbltitle=Label(app,text="SOCIAL").grid(row=6, column=1, padx=100 , pady=20)


inputf=Entry(app, width=50)
inputf.grid(row=6, column=2)



btnAdd=Button(app,text="INSERT",command=insertvalues).grid(row=10,column=1)


btnAdd=Button(app,text="UPDATE",command=updatevalues).grid(row=10,column=2)

btnAdd=Button(app,text="DELETE",command=deletevalues).grid(row=11,column=1)


btnAdd=Button(app,text="SUBMIT").grid(row=11,column=2)
















app.mainloop()