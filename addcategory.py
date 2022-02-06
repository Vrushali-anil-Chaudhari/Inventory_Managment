from tkinter import *
from PIL import ImageTk
from tkinter import messagebox




def addc(root):
    root=Tk()
    root.geometry("400x200")
    root.title("Add Category")
    root.bg=ImageTk.PhotoImage(file="C:/Users/vrush/OneDrive/Desktop/Mini_Proj/loginbgimg.png")
    root.bg_image=Label(root, image=root.bg).place(x=0,y=0,relwidth=1,relheight=1)
    root.iconbitmap('C:/Users/vrush/OneDrive/Desktop/Mini_Proj/loginicon.ico')
    categoryname=Label(root,text="Name of Category", bd= "5",bg="green",relief=RIDGE,
                   font=("times new roman",12,"bold"),fg="black", borderwidth=2,padx=3,pady=3)
    categoryname.grid(row=0,column=0,pady=40,padx=40)


    e=Entry(root)
    e.grid(row=0,column=1, padx=5,pady=5)

    buttonadddetail = Button(root, text="Submit", padx=2, pady=2, bd=5, fg="Black", bg="Grey",
                         font=("times new roman", 12, "bold"))
    buttonadddetail.place(x=150, y=150)
    categoryname1 = Label(root, text=group, bd="5", bg="green", relief=RIDGE,
                         font=("times new roman", 12, "bold"), fg="black", borderwidth=2, padx=3, pady=3)
    categoryname1.grid(row=1, column=0, pady=40, padx=40)

    root.mainloop()
