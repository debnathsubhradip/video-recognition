# import Human_Recognition as hr
# import  folder_control as fc
# import os
import time
from tkinter import *
t1=""
root = Tk()
m1 = Label(root, text=t1,pady=5,width=50,height=5)
def mes():
    m1 = Label(root, text=t1)
    m1.pack()

def welcome():
    t1="Welcome User"
    mes()
    time.sleep(1)
    print("Check")
    # m1.destroy()
var = IntVar()
def checkval ():
    if var.get() ==1:
        m1.destroy()
        time.sleep(.8)
        welcome()
def init ():

    menu=Menu(root)
    filemenu=Menu(menu)
    menu.add_cascade(label="File",menu=filemenu)
    filemenu.add_command(label="Command Panel",command=welcome)

    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=root.quit)
        # menu.grid(row="0",column="0")

    c1=Checkbutton(root, text = "Enable Human Recognition", variable=var, onvalue = 1, offvalue =0, height = 4, width = 20, pady =3 )

    c1.pack()
    b1=Button(root, text = "Update Command", command = checkval, height = 4, width = 20, pady = 5)
    b1.pack()
    root.config(menu=menu)
    root.mainloop()
init()