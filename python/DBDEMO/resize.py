from tkinter import *
from PIL import Image, ImageTk


win=Tk()


win.geometry("700x350")


image=Image.open('img3.jpg')


img=image.resize((100, 50))


my_img=ImageTk.PhotoImage(img)


label=Label(win, image=my_img)
label.pack()

win.mainloop()
