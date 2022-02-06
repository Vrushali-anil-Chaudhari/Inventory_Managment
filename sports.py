from tkinter import *
from PIL import ImageTk

import additemmens
import qrcode
import table


def content(root):
        def qr(group):
            q=Toplevel(root)
            qrcode.qrcode(q,group)

        def viewdetails(group):
          view = Toplevel(root)
          table.viewdetail(view, group)

        def adddetails(group):
          add = Toplevel(root)
          additemmens.addcategories(add, group)

        root.title("Inventory management system")
        root.geometry("1350x800+0+0")
        root.iconbitmap('C:/Users/vrush/OneDrive/Desktop/Mini_Proj/loginicon.ico')
        root.bg=ImageTk.PhotoImage(file="C:/Users/vrush/OneDrive/Desktop/Mini_Proj/loginbgimg.png")
        root.bg_image=Label(root, image=root.bg).place(x=0,y=0,relwidth=1,relheight=1)

        lbltitle=Label(root,text="Grocery",bg="powder blue",fg="black",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        #===============================ele=================================

        Frameelectronic = LabelFrame(root,text="Sports Wear", bd=12,relief=RIDGE,padx=20,bg="powder blue",font=("times new roman",12,"bold"))
        Frameelectronic.place(x=20,y=200,width=240,height=240)

        buttonviewdetail = Button(root, text="View Details", padx=2, pady=2,bd=10,fg="white",bg="purple",font=("times new roman",12,"bold"),command=lambda :viewdetails("sportsw"))
        buttonviewdetail.place(x=75, y=250)
        buttonadd = Button(root, text="QR Code", padx=2, pady=2,bd=10,fg="white",bg="purple",font=("times new roman",12,"bold"),command=lambda :qr("sportsw"))
        buttonadd.place(x=85, y=370)
        buttonadddetail = Button(root, text="Add Details", padx=2, pady=2, bd=10, fg="white", bg="purple",
                                 font=("times new roman", 12, "bold"),command=lambda: adddetails("sportsw"))
        buttonadddetail.place(x=77, y=310)


        #===================================== clothing =========================================
        Frameclothing = LabelFrame(root, text="Gym Equipments", bd=12, relief=RIDGE, padx=20, bg="powder blue",
                                   font=("times new roman", 12, "bold"),)
        Frameclothing.place(x=350, y=200, width=240, height=240)


        buttonviewdetail = Button(root, text="View Details", padx=2, pady=2, bd=10, fg="white", bg="purple",
                                  font=("times new roman", 12, "bold"),command=lambda :viewdetails("gym"))
        buttonviewdetail.place(x=405, y=250)
        buttonadd = Button(root, text="QR Code", padx=2, pady=2, bd=10, fg="white", bg="purple",
                           font=("times new roman", 12, "bold"),command=lambda :qr("gym"))
        buttonadd.place(x=415, y=370)

        buttonadddetail = Button(root, text="Add Details", padx=2, pady=2, bd=10, fg="white", bg="purple",
                                 font=("times new roman", 12, "bold"),command=lambda: adddetails("gym"))
        buttonadddetail.place(x=407, y=310)

        #=====================================Sports Accessories =====================================

        Framegrocery = LabelFrame(root, text="Sports Accessories", bd=12, relief=RIDGE, padx=20, bg="powder blue",
                                  font=("times new roman", 12, "bold"))
        Framegrocery.place(x=685, y=200, width=240, height=240)

        buttonviewdetail = Button(root, text="View Details", padx=2, pady=2, bd=10, fg="white", bg="purple",
                                  font=("times new roman", 12, "bold"),command=lambda :viewdetails("SportsAccessories"))
        buttonviewdetail.place(x=745, y=250)
        buttonadd = Button(root, text="QR Code", padx=2, pady=2, bd=10, fg="white", bg="purple",
                           font=("times new roman", 12, "bold"),command=lambda :qr("SportsAccessories"))
        buttonadd.place(x=755, y=370)

        buttonadddetail = Button(root, text="Add Details", padx=2, pady=2, bd=10, fg="white", bg="purple",
                                 font=("times new roman", 12, "bold"),command=lambda: adddetails("SportsAccessories"))
        buttonadddetail.place(x=747, y=310)

        #add category ==============================================================================

        Frameaddcategory = LabelFrame(root, text="Add Item", bd=12, relief=RIDGE, padx=20, bg="powder blue",
                                      font=("times new roman", 12, "bold"))
        Frameaddcategory.place(x=1025, y=200, width=240, height=240)

        buttonviewdetail = Button(root, text="Add Item", padx=10, pady=10, bd=10, fg="white", bg="purple",
                                  font=("times new roman", 12, "bold"))
        buttonviewdetail.place(x=1090, y=280)

        root.mainloop()