import sqlite3
from tkinter import *
from tkinter import messagebox

import categoryfirstpage


def newscreen():
    new = Toplevel(root)
    categoryfirstpage.mainscreen(new)




def Submit():
    c.execute('insert into inventory values(?,?)',(e1.get(),e2.get()))
    conn.commit()
def signin():
     c.execute('select * from inventory  ')
     r = c.fetchall()
     count=1
     for i in r:
        if(i[0]==e1.get() and i[1]==int(e2.get())):
           count=1
           break
        else:
            count=0

     if(count==1):
         messagebox.showinfo("showinfo", "Valid")
         newscreen()
     elif(count==0):
         messagebox.showinfo("showinfo", "InValid")


conn=sqlite3.connect("C:/Users/vrush/OneDrive/Desktop/Mini_Proj/inventroy.db")
c=conn.cursor()
root=Tk()
root.geometry("300x300")
root.title("Login Screen")
Name=Label(root,text="Username")
Name.grid(row=0,column=0,pady=10,padx=20)
Password=Label(root,text="Password")
Password.grid(row=1,column=0,pady=10,padx=20)
Button1=Button(root,text="Register",command=Submit)
Button1.place(x=50,y=90)
Button2=Button(root,text="Quit",command=root.quit)
Button2.place(x=110,y=130)
Button3=Button(root,text="Log in",command=signin)
Button3.place(x=150,y=90)

e1=Entry(root)
e1.grid(row=0,column=1)

e2=Entry(root,show='*')
e2.grid(row=1,column=1)

root.mainloop()