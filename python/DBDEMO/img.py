from tkinter import *
from PIL import ImageTk, Image

win = Tk()


win.geometry("700x500")

frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

img = ImageTk.PhotoImage(Image.open("img3.jpg"),width=200,height=100)

label = Label(frame, image = img)
label.pack()

win.mainloop()