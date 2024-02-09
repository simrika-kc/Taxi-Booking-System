from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from PIL import Image as image ,ImageTk

from Controller.admin_controll import booking_details
from Controller.driver_controll import assigned_booking_details, complete_booking
from Model.booking import Booking
from View.assign_drivers import AssignDriver
from View.booking_table import BookingTable
from View.customer_table import CustomerTable
from View.driver_booking_table import DriverBookingTable
from View.driver_profile import DriverProfile
from driver_table import *
class DriverBoard:
    def __init__(self,window):
        self.window=window

        self.window.title("Taxi booking system")
        self.dashFrame() #calling dashFrame function

        self.booking_status = None


    def dashFrame(self):
        self.window.state("zoomed")
        self.window.configure(bg="#F1EAFF")

        self.framethird=Frame(self.window,width=1213,height=544,bg="#B0A695",borderwidth=1,relief="solid")
        self.framethird.place(x=311,y=122)

        self.booking_label = Label(self.framethird, text="Assigned Booking Information", font=("Rockwell", 30, "bold"), fg="black",bg="#B0A695")
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
        self.tree.bind("<ButtonRelease-1>", self.select_booking)


        self.showin_table()

        self.frame = Frame(self.window, width=1530, height=70, bg="#2c2c2c",borderwidth=1,relief="solid")  # making frame
        self.frame.place(x=2, y=2)  # placing frame

        self.framesecond = Frame(self.window, width=1530, height=40, bg="#5c5c5c",borderwidth=1,relief="solid")  # making frame
        self.framesecond.place(x=2, y=71)  # placing frame

        # for booking id
        self.booking_id = Label(self.framethird, text="Booking ID : ", font=("Times new roman", 16, "bold"), fg="black",
                                bg="#B0A695")
        self.booking_id.place(x=450, y=370)

        self.booking_entry = Entry(self.framethird, width=8, font=("Times new roman", 18,))
        self.booking_entry.place(x=600, y=370)

        # complete button
        self.complete_Button = Button(self.framethird, text="Complete", width=17, height=1, bg="#65B741",
                                    fg="white", font=("Times new roman", 15, "bold"),command=self.complete_booking )
        self.complete_Button.place(x=480, y=450)

 #for Navigation
        self.lbl_Heading=Label(self.frame,text="Taxi Booking System",fg="white",bg="#2c2c2c",font=("Times new roman",30,"bold"))
        self.lbl_Heading.place(x=75,y=10)

        self.lbl_Gallary = Label(self.framesecond, text="Welcome to Driver Page!!", fg="white", bg="#5c5c5c", font=("Times new roman", 20, "bold"))
        self.lbl_Gallary.place(x=4, y=0)

#icon image
        self.imagecar = image.open("Images/cars.png")
        self.photocar = ImageTk.PhotoImage(self.imagecar)

        self.image_iconcar = Label(self.frame, image=self.photocar, bg="#2c2c2c")
        self.image_iconcar.place(x=0, y=0)

        self.booknow=Label(self.framesecond,text="Taxi booking system", width=15, height=1,bg="#5c5c5c", fg="white",font=("Times new roman",14,"bold"))
        self.booknow.place(x=1320, y=10)

#for content
        self.second_Frame=Frame(self.window,width=295,height=665,bg="#5c5c5c")
        self.second_Frame.place(x=3,y=109)

        self.image = image.open("Images/admin.png")
        self.photo = ImageTk.PhotoImage(self.image)

        self.image_content=Label(self.second_Frame,image=self.photo,bg="#5c5c5c")
        self.image_content.place(x=0,y=4)

        #for booknow
        self.bookimg=image.open("Images/pp.png")
        self.bookpic=ImageTk.PhotoImage(self.bookimg)

        self.imagebook=Label(self.second_Frame,image=self.bookpic,bg="#5c5c5c")
        self.imagebook.place(x=15,y=372)

        self.booknow=Label(self.second_Frame,text="Profile",cursor="hand2",font=("Times new roman", 15, "bold"), fg="black",bg="#5c5c5c")
        self.booknow.place(x=80,y=385)
        self.booknow.bind("<Button-1>",self.driver_table)

        #for profile
        self.profileimg = image.open("Images/book.png")
        self.profilepic = ImageTk.PhotoImage(self.profileimg)

        self.imageprofile = Label(self.second_Frame, image=self.profilepic, bg="#5c5c5c")
        self.imageprofile.place(x=15, y=310)

        self.booking = Label(self.second_Frame, text="Booking Info.",cursor="hand2", font=("Times new roman", 15, "bold"), fg="black",bg="#5c5c5c")
        self.booking.place(x=80, y=330)
        self.booking.bind("<Button-1>", self.booking_table)

        # last frame
        self.framelast = Frame(self.window, width=1530, height=110, bg="#3c3c3c", borderwidth=1,relief="solid")  # making frame
        self.framelast.place(x=2, y=681)  # placing frame

        # labels for content
        self.label_content=Label(self.framelast,text="Taxi Booking System|||Developed by Simrika K.C ",font=("Times new roman", 17, "bold"), bg="#3c3c3c",fg="black")
        self.label_content.place(x=600,y=10)

        self.label_text=Label(self.framelast,text="For any suppport:",font=("Times new roman", 17, "bold"), bg="#3c3c3c",fg="black")
        self.label_text.place(x=680,y=40)

        self.label_Contact = Label(self.framelast, text="Contact: 9860236768", width=15, height=1, fg="black", bg="#3c3c3c",font=("Times new roman",17,"underline"))
        self.label_Contact.place(x=690, y=70)

        self.logout_button = Button(self.window, text="Logout", width=7, height=1, bg="white", fg="red",font=("Times new roman", 17, "bold"), command=self.logout)
        self.logout_button.place(x=1385, y=10)

    def driver_table(self,event):
        self.framethird.destroy()  # to remove frame
        drivertable=DriverProfile(self.window) #making object of driver_table page class.


    def booking_table(self,event):
        self.framethird.destroy()
        tablebooking=DriverBookingTable(self.window)

    def showin_table(self):

        fortable = assigned_booking_details()
        print(fortable)

        for row in self.tree.get_children():  #to delete the existing data
            self.tree.delete(row)

        for result in fortable:  #for inserting data in table
            self.tree.insert('', END, values=result)

    def select_booking(self, event):
        values = self.tree.focus()
        bookings = self.tree.item(values)

        row = bookings.get('values')
        self.booking_entry.delete(0, END)
        self.booking_entry.insert(0, row[0])
        self.booking_status = row[6]

    def complete_booking(self):
        #get value from entry field
        booking_id = self.booking_entry.get()
        #validating
        if booking_id != "":
            if self.booking_status != "Completed":
                booking = Booking(booking_id=booking_id)
                complete = complete_booking(booking)
                if complete == True:
                    messagebox.showinfo("SUCCESS", "Successfully Completed Booking !")
                    self.showin_table()
                    self.booking_status = ""
                else:
                    messagebox.showerror("ERROR", "Couldn't Complete Booking !")
            else:
                messagebox.showerror("ERROR", "Booking Already Completed")

        else:
            messagebox.showerror("ERROR", "Please Select Booking From The Table.")

    def logout(self):
        from login_page import LoginPage
        self.window.destroy()

        root = Tk()
        LoginPage(root)
        root.mainloop()

if __name__ == '__main__':
    window=Tk()
    dashboard=DriverBoard(window)
    window.mainloop()