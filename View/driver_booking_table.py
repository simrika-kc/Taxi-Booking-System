from PIL import Image as image, ImageTk
from tkinter import ttk, messagebox
from tkinter import *

from Controller.admin_controll import booking_details
from Controller.customer_booking import for_table
from Controller.driver_controll import assigned_booking_details, complete_booking
from Model import global_variable
from Model.booking import Booking


class DriverBookingTable: #making class
    def __init__(self, window):
        self.window = window

        self.window.title("Taxi booking system")  # setting title
        self.booking_info() # calling driver_info function

        self.booking_status = None


    def booking_info(self):
        self.frame=Frame(self.window,width=1213,height=544,bg="#B0A695",borderwidth=1,relief="solid")
        self.frame.place(x=311,y=122)

        self.driver_label = Label(self.frame, text="Assigned Booking Information", font=("Rockwell", 30, "bold"), fg="black",bg="#B0A695")
        self.driver_label.place(x=425, y=25)

        # for booking id
        self.booking_id = Label(self.frame, text="Booking ID : ",font=("Times new roman", 16, "bold"), fg="black", bg="#B0A695")
        self.booking_id.place(x=450, y=370)

        self.booking_entry = Entry(self.frame, width=8, font=("Times new roman", 18,))
        self.booking_entry.place(x=600, y=370)

      #complete button
        self.assign_Button = Button(self.frame, text="Complete", width=17, height=1, bg="#65B741",
                                      fg="white", font=("Times new roman", 15, "bold"),command=self.complete_booking)
        self.assign_Button.place(x=480, y=450)


        # adding jtable
        self.column=("Booking_ID","Customer ID","Pickup Address","Dropoff Address","Pickup Date","driver_id","Status")
        self.tree=ttk.Treeview(self.frame,columns=self.column,show="headings")

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


    def showin_table(self):

        fortable = assigned_booking_details()

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
        booking_id = self.booking_entry.get()
        if booking_id !="":
            if self.booking_status != "Completed":
                booking = Booking(booking_id = booking_id)
                complete = complete_booking(booking)
                if complete == True:
                    messagebox.showinfo("SUCCESS", "Successfully Completed Booking !")
                    self.showin_table()  # Refresh the tree/table to reflect changes
                    self.booking_status = ""
                else:
                    messagebox.showerror("ERROR", "Couldn't Complete Booking !")
            else:
                messagebox.showerror("ERROR", "Booking Already Completed")

        else:
            messagebox.showerror("ERROR", "Please Select Booking From The Table.")



if __name__ == '__main__':
    window = Tk()
    bookingtable = DriverBookingTable(window)
    window.mainloop()