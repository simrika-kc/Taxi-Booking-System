from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from PIL import Image ,ImageTk
from tkinter import messagebox
from Controller.customer_booking import booking_taxi, for_table, update_booking, cancel_booking
from Model import global_variable
from Model.booking import Booking


class DashBoard:
    def __init__(self,window):

        self.window=window
        self.window.title("Taxi booking system")
        self.window.resizable(0,0)
        self.dashFrame() #calling dashFrame function

        self.booking_id = 0

    def dashFrame(self):
        self.window.state("zoomed")
        self.window.configure(bg="#F1EAFF")

        self.framethird = Frame(self.window, width=1280, height=544, bg="#DCBFFF", borderwidth=1, relief="solid")
        self.framethird.place(x=246, y=122)

        # adding jtable
        self.column = ("Booking_ID", "Pickup Address", "Dropoff Address", "Pickup Date", "Status", "Driver ID")
        self.tree = ttk.Treeview(self.framethird, columns=self.column, show="headings")

        for col in self.column:
            self.tree.heading(col, text=col)

        self.tree.place(x=29, y=300)

        self.tree.bind("<ButtonRelease-1>", self.select_booking)

        self.showin_table()


        self.frame = Frame(self.window, width=1530, height=70, bg="#DCBFFF",borderwidth=1,relief="solid")  # making frame
        self.frame.place(x=2, y=0)  # placing frame

        self.framesecond = Frame(self.window, width=1530, height=40, bg="#D0A2F7",borderwidth=1,relief="solid")  # making frame
        self.framesecond.place(x=2, y=71)  # placing frame

 #for Navigation
        self.lbl_Heading=Label(self.frame,text="Taxi Booking System",fg="black",bg="#DCBFFF",font=("Times new roman",30,"bold"))
        self.lbl_Heading.place(x=75,y=10)

        self.lbl_Gallary = Label(self.framesecond, text="Welcome Simrika!!", fg="black", bg="#D0A2F7", font=("Times new roman", 20, "bold"))
        self.lbl_Gallary.place(x=4, y=3)

#icon image
        self.imagecar = Image.open("Images/cars.png")
        self.photocar = ImageTk.PhotoImage(self.imagecar)

        self.image_iconcar = Label(self.frame, image=self.photocar, bg="#DCBFFF")
        self.image_iconcar.place(x=0, y=0)

        self.booknow=Label(self.framesecond,text="Taxi booking system", width=15, height=1,bg="#D0A2F7", fg="white",font=("Times new roman",14,"bold"))
        self.booknow.place(x=1320, y=10)

#for content
        self.second_Frame=Frame(self.window,width=230,height=665,bg="#DCBFFF")
        self.second_Frame.place(x=3,y=109)

        self.image = Image.open("Images/taxi_content.png")
        self.photo = ImageTk.PhotoImage(self.image)

        self.image_content=Label(self.second_Frame,image=self.photo,bg="#DCBFFF")
        self.image_content.place(x=0,y=4)

#for booknow
        self.bookimg=Image.open("Images/book.png")
        self.bookpic=ImageTk.PhotoImage(self.bookimg)

        self.imagebook=Label(self.second_Frame,image=self.bookpic,bg="#DCBFFF")
        self.imagebook.place(x=15,y=372)

        self.booknow=Label(self.second_Frame,text="Book Now ",cursor="hand2",font=("Times new roman", 18, "bold"), fg="black",bg="#DCBFFF")
        self.booknow.place(x=80,y=385)
        #for profile
        self.profileimg = Image.open("Images/pp.png")
        self.profilepic = ImageTk.PhotoImage(self.profileimg)

        self.imageprofile = Label(self.second_Frame, image=self.profilepic, bg="#DCBFFF")
        self.imageprofile.place(x=15, y=320)

        self.profile = Label(self.second_Frame, text="Profile",cursor="hand2", font=("Times new roman", 18, "bold"), fg="black",bg="#DCBFFF")
        self.profile.place(x=80, y=330)
        self.profile.bind("<Button-1>", self.show_profile)


        #for exit
        self.exitsimg = Image.open("Images/exit.png")
        self.exitspic = ImageTk.PhotoImage(self.exitsimg)

        self.imageexit = Label(self.second_Frame, image=self.exitspic, bg="#DCBFFF")
        self.imageexit.place(x=25, y=435)

        self.exit = Label(self.second_Frame, text="Exit",cursor="hand2", font=("Times new roman", 18, "bold"), fg="black",bg="#DCBFFF")
        self.exit.place(x=80, y=439)

        # last frame
        self.framelast = Frame(self.window, width=1530, height=110, bg="#DCBFFF", borderwidth=1,
                               relief="solid")  # making frame
        self.framelast.place(x=2, y=681)  # placing frame

        # labels for content
        self.label_content=Label(self.framelast,text="Taxi Booking System|||Developed by Simrika K.C ",font=("Times new roman", 15, "bold"), fg="black",bg="#DCBFFF")
        self.label_content.place(x=600,y=10)

        self.label_text=Label(self.framelast,text="For any suppport:",font=("Times new roman", 15, "bold"), fg="black",bg="#DCBFFF")
        self.label_text.place(x=680,y=40)

        self.label_Contact = Label(self.framelast, text="Contact: 9860236768", width=15, height=1, bg="#DCBFFF", fg="black",font=("Times new roman",15,"underline"))
        self.label_Contact.place(x=690, y=70)

        self.logout_button = Button(self.window, text="Logout", width=7, height=1, bg="#DCBFFF", fg="red",font=("Times new roman", 17, "bold"), command=self.logout)
        self.logout_button.place(x=1385, y=10)

        #for thirdframe content
        #pickup location
        self.pickuplocation = Label(self.framethird, text="Pickup Location : ", font=("Times new roman", 16, "bold"), fg="black",bg="#DCBFFF")
        self.pickuplocation.place(x=50, y=70)

        self.pickentry = Entry(self.framethird, width=14, font=("Times new roman", 18,))
        self.pickentry.place(x=220, y=70)

        #dropOff location
        self.dropofflocation = Label(self.framethird, text="Dropoff Location : ", font=("Times new roman", 16, "bold"), fg="black",bg="#DCBFFF")
        self.dropofflocation.place(x=420, y=70)

        self.dropoffentry = Entry(self.framethird, width=14, font=("Times new roman", 18,))
        self.dropoffentry.place(x=605, y=70)

        #pickup date
        self.date = Label(self.framethird, text="Pickup date : ", font=("Times new roman", 16, "bold"),fg="black", bg="#DCBFFF")
        self.date.place(x=810, y=70)

        self.dateentry =DateEntry(self.framethird, width=14, font=("Times new roman", 18,),date_pattern='dd/mm/yyyy')
        self.dateentry.place(x=945, y=70)

        #book buttons
        self.book_Button=Button(self.framethird,text="Book",width=16,height=1,bg="#7B66FF",fg="white",font=("Times new roman",15,"bold"),command=self.booking)
        self.book_Button.place(x=180,y=170)


        #update button
        self.register_Button=Button(self.framethird,text="Update Booking",width=17,height=1,bg="#65B741",fg="white",font=("Times new roman",15,"bold"),command=self.update_bookings)
        self.register_Button.place(x=460,y=170)
        # delete button
        self.delete_Button=Button(self.framethird,text="Delete Booking",width=17,height=1,bg="#EF4040",fg="white",font=("Times new roman",15,"bold"),command=self.cancel_bookings)
        self.delete_Button.place(x=770,y=170)

    def booking(self):
        pickentry=self.pickentry.get()
        dropoffentry=self.dropoffentry.get()
        dateentry=self.dateentry.get()
        if pickentry=="" or dropoffentry=="" or dateentry=="":    #validating these fields
            messagebox.showerror("Error","Fill all the details")
        else:
        #making object of class booking from model
            booking=Booking(pickup_date=dateentry,pickup_address=pickentry,dropoff_address=dropoffentry,status="Pending",customer_id=global_variable.customer[0])
            booking=booking_taxi(booking)

            if booking==True:
              messagebox.showinfo("book","Successfully booked")
              self.clear_function()
              self.showin_table()
            else:
              messagebox.showerror("error","Sorry! cannot book ")

    def showin_table(self):
        booking=Booking(customer_id=global_variable.customer[0])

        fortable = for_table(booking)

        for row in self.tree.get_children():  #to delete the existing data
            self.tree.delete(row)

        for result in fortable:  #for inserting data in table
            self.tree.insert('', END, values=result)

    # to select row from the table
    def select_booking(self, event):
        values = self.tree.focus()
        bookings = self.tree.item(values)

        row = bookings.get('values')

        # to clear the field first
        self.clear_function()

        self.booking_id = row[0]
        self.pickentry.insert(0, row[1])
        self.dropoffentry.insert(0, row[2])
        self.dateentry.insert(0, row[3])


    def clear_function(self):
        self.pickentry.delete(0,END)
        self.dropoffentry.delete(0,END)
        self.dateentry.delete(0,END)
    def update_bookings(self):
        #get values from entry field
        pickentry = self.pickentry.get()
        dropoffentry = self.dropoffentry.get()
        dateentry = self.dateentry.get()

        if self.booking_id !=0:
            if pickentry=="" or dropoffentry=="" or dateentry=="":
                messagebox.showerror("error","Fill all the field")  #checking if the field is empty
            else: #making object of Booking class
                booking = Booking(pickup_address=pickentry, dropoff_address=dropoffentry, pickup_date=dateentry,
                                  booking_id=self.booking_id, status="pending")
                updatebooking = update_booking(booking)

                if updatebooking==True:
                    messagebox.showinfo("success","Successfully updated")
                    self.showin_table()

                else:
                    messagebox.showerror("error","Cannot Update")
        else:
            messagebox.showerror("error", "Please select booking from the table.")

    def cancel_bookings(self):
        if self.booking_id != 0:
                booking = Booking(booking_id=self.booking_id, status="pending")
                cancelbooking = cancel_booking(booking)

                if cancelbooking == True:
                    messagebox.showinfo("success", "Successfully Canceled")
                    self.showin_table()  # Refresh the table to reflect the changes

                else:
                    messagebox.showerror("error", "Cannot Cancel")
        else:
            messagebox.showerror("error", "Please select booking from the table.")

    # Open a new top-level window for displaying the profile
    def show_profile(self, event):
        self.top_level = Toplevel(self.window, width=800, height=600)



    def logout(self):
        from login_page import LoginPage
        self.window.destroy()

        root = Tk()
        LoginPage(root)
        root.mainloop()

if __name__ == '__main__':
    window=Tk()
    dashboard=DashBoard(window)
    window.mainloop()
