from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from PIL import Image as image ,ImageTk

from Controller.admin_controll import booking_details
from View.assign_drivers import AssignDriver
from View.booking_table import BookingTable
from View.customer_table import CustomerTable
from driver_table import *
class AdminBoard:
    def __init__(self,window):
        self.window=window

        self.window.title("Taxi booking system")
        self.dashFrame() #calling dashFrame function

    def dashFrame(self):
        self.window.state("zoomed")
        self.window.configure(bg="#F1EAFF")

        self.framethird=Frame(self.window,width=1213,height=544,bg="#B0A695",borderwidth=1,relief="solid")
        self.framethird.place(x=311,y=122)

        self.booking_label = Label(self.framethird, text="Bookings Informations", font=("Rockwell", 30, "bold"), fg="black",bg="#B0A695")
        self.booking_label.place(x=425, y=25)

        #adding jtable
        self.column=("Booking_ID","Customer ID","Pickup Address","Dropoff Address","Pickup Date","driver_id","Status")
        self.tree=ttk.Treeview(self.framethird,columns=self.column,show="headings")

        for col in self.column:
            self.tree.heading(col,text=col)
            self.tree.place(x=5,y=100)

        self.tree.column("Booking_ID", width=160, anchor="center")
        self.tree.column("Customer ID", width=160, anchor="center")
        self.tree.column("Pickup Address", width=180, anchor="center")
        self.tree.column("Dropoff Address", width=160, anchor="center")
        self.tree.column("Pickup Date", width=180, anchor="center")
        self.tree.column("driver_id", width=180, anchor="center")
        self.tree.column("Status", width=180, anchor="center")

        self.showin_table()

        self.frame = Frame(self.window, width=1530, height=70, bg="#776B5D",borderwidth=1,relief="solid")  # making frame
        self.frame.place(x=2, y=2)  # placing frame

        self.framesecond = Frame(self.window, width=1530, height=40, bg="#B0A695",borderwidth=1,relief="solid")  # making frame
        self.framesecond.place(x=2, y=71)  # placing frame

 #for Navigation
        self.lbl_Heading=Label(self.frame,text="Taxi Booking System",fg="black",bg="#776B5D",font=("Times new roman",30,"bold"))
        self.lbl_Heading.place(x=75,y=10)

        self.lbl_Gallary = Label(self.framesecond, text="Welcome in Admin Page!!", fg="white", bg="#B0A695", font=("Times new roman", 20, "bold"))
        self.lbl_Gallary.place(x=4, y=0)

#icon image
        self.imagecar = image.open("Images/cars.png")
        self.photocar = ImageTk.PhotoImage(self.imagecar)

        self.image_iconcar = Label(self.frame, image=self.photocar, bg="#776B5D")
        self.image_iconcar.place(x=0, y=0)

        self.booknow=Label(self.framesecond,text="Taxi booking system", width=15, height=1,bg="#B0A695", fg="white",font=("Times new roman",14,"bold"))
        self.booknow.place(x=1320, y=10)

#for content
        self.second_Frame=Frame(self.window,width=295,height=665,bg="#B0A695")
        self.second_Frame.place(x=3,y=109)

        self.image = image.open("Images/admin.png")
        self.photo = ImageTk.PhotoImage(self.image)

        self.image_content=Label(self.second_Frame,image=self.photo,bg="#B0A695")
        self.image_content.place(x=0,y=4)

        #for booknow
        self.bookimg=image.open("Images/book.png")
        self.bookpic=ImageTk.PhotoImage(self.bookimg)

        self.imagebook=Label(self.second_Frame,image=self.bookpic,bg="#B0A695")
        self.imagebook.place(x=15,y=372)

        self.booknow=Label(self.second_Frame,text="Drivers Info.",cursor="hand2",font=("Times new roman", 15, "bold"), fg="black",bg="#B0A695")
        self.booknow.place(x=80,y=385)
        self.booknow.bind("<Button-1>",self.driver_table)

        #for profile
        self.profileimg = image.open("Images/pp.png")
        self.profilepic = ImageTk.PhotoImage(self.profileimg)

        self.imageprofile = Label(self.second_Frame, image=self.profilepic, bg="#B0A695")
        self.imageprofile.place(x=15, y=320)

        self.profile = Label(self.second_Frame, text="Customers Info.",cursor="hand2", font=("Times new roman", 15, "bold"), fg="black",bg="#B0A695")
        self.profile.place(x=80, y=330)
        self.profile.bind("<Button-1>", self.customer_table)

        #for bills
        self.billsimg = image.open("Images/bill.png")
        self.billspic = ImageTk.PhotoImage(self.billsimg)

        self.imagebills = Label(self.second_Frame, image=self.billspic, bg="#B0A695")
        self.imagebills.place(x=15, y=430)

        self.bills = Label(self.second_Frame, text="Bookings Info.",cursor="hand2", font=("Times new roman", 15, "bold"), fg="black",bg="#B0A695")
        self.bills.place(x=80, y=439)
        self.bills.bind("<Button-1>",self.booking_table)

        #for Assign drivers

        self.assign_drivers_label = Label(self.second_Frame, text="Assign Drivers",cursor="hand2", font=("Times new roman", 15, "bold"), fg="black",bg="#B0A695")
        self.assign_drivers_label.place(x=50, y=490)

        self.assign_drivers_label.bind("<Button-1>",self.assign_drivers_function)

        # last frame
        self.framelast = Frame(self.window, width=1530, height=110, bg="#776B5D", borderwidth=1,
                               relief="solid")  # making frame
        self.framelast.place(x=2, y=681)  # placing frame

        # labels for content
        self.label_content=Label(self.framelast,text="Taxi Booking System|||Developed by Simrika K.C ",font=("Times new roman", 17, "bold"), bg="#776B5D",fg="black")
        self.label_content.place(x=600,y=10)

        self.label_text=Label(self.framelast,text="For any suppport:",font=("Times new roman", 17, "bold"), bg="#776B5D",fg="black")
        self.label_text.place(x=680,y=40)

        self.label_Contact = Label(self.framelast, text="Contact: 9860236768", width=15, height=1, fg="black", bg="#776B5D",font=("Times new roman",17,"underline"))
        self.label_Contact.place(x=690, y=70)

        self.logout_button = Button(self.window, text="Logout", width=7, height=1, bg="white", fg="red",font=("Times new roman", 17, "bold"), command=self.logout)
        self.logout_button.place(x=1385, y=10)

    def driver_table(self,event):
        self.framethird.destroy()  # to remove frame
        drivertable=DriverTable(self.window) #making object of driver_table page class.

    def customer_table(self,event):
        self.framethird.destroy()
        customertable=CustomerTable(self.window)

    def assign_drivers_function(self,event):
        self.framethird.destroy()
        assigndriver=AssignDriver(self.window)

    def booking_table(self,event):
        self.framethird.destroy()
        tablebooking=BookingTable(self.window)

    def showin_table(self):

        fortable = booking_details()
        print(fortable)

        for row in self.tree.get_children():  #to delete the existing data
            self.tree.delete(row)

        for result in fortable:  #for inserting data in table
            self.tree.insert('', END, values=result)

    def logout(self):
        from login_page import LoginPage
        self.window.destroy()

        root = Tk()
        LoginPage(root)
        root.mainloop()

if __name__ == '__main__':
    window=Tk()
    dashboard=AdminBoard(window)
    window.mainloop()