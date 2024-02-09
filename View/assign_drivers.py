from tkinter import *
from tkinter import messagebox
from PIL import Image as image, ImageTk
from tkinter import ttk

from Controller.admin_controll import showbookings, assign_driver
from Model import global_variable
from Model.booking import Booking


class AssignDriver: #making class
    def __init__(self, window):
        self.window = window

        self.window.title("Taxi booking system")  # setting title
        self.assigndriver_info() # calling assigndriver_info function


    def assigndriver_info(self):
        self.frame=Frame(self.window,width=1213,height=544,bg="#B0A695",borderwidth=1,relief="solid")
        self.frame.place(x=311,y=122)

        self.driver_label = Label(self.frame, text="Drivers Assign", font=("Rockwell", 30, "bold"), fg="black",bg="#B0A695")
        self.driver_label.place(x=425, y=18)


        # adding jtable
        self.column = ("Booking_id", "customer_id", "pickup_Address", "pickup_date","dropoff_address","Booking_status")
        self.tree = ttk.Treeview(self.frame, columns=self.column, show="headings")

        for col in self.column:
            self.tree.heading(col, text=col)
        self.tree.place(x=5, y=95)
        self.tree.bind("<ButtonRelease-1>", self.select_booking)
        self.showtreetabel()
    def showtreetabel(self):
        showbooking=showbookings()

        for row in self.tree.get_children():#to delete the existing data
            self.tree.delete(row)
        for result in showbooking:
            self.tree.insert('',END,values=result)



#for customer id
        self.cus_id = Label(self.frame, text="Booking ID : ",
                                        font=("Times new roman", 16, "bold"), fg="black", bg="#B0A695")
        self.cus_id.place(x=280, y=370)

        self.cus_id_entry= Entry(self.frame, width=8, font=("Times new roman", 18,))
        self.cus_id_entry.place(x=420, y=370)

     #for assign driver
        self.assigndriver = Label(self.frame, text="Assign driver: ",
                            font=("Times new roman", 16, "bold"), fg="black", bg="#B0A695")
        self.assigndriver.place(x=580, y=370)

        self.assigndriver_entry = Entry(self.frame, width=14, font=("Times new roman", 18,))
        self.assigndriver_entry.place(x=720, y=370)

        # Assign button
        self.assign_Button = Button(self.frame, text="Assign", width=17, height=1, bg="#65B741",
                                      fg="white", font=("Times new roman", 15, "bold"), command=self.assign_Driver)
        self.assign_Button.place(x=480, y=450)

    def select_booking(self,event):
        values = self.tree.focus()
        bookings = self.tree.item(values)

        row = bookings.get('values')

        print(row)

        # to clear the field first
        self.cus_id_entry.delete(0,END)
        self.cus_id_entry.insert(0,row[0])

        if global_variable.driver_id !=0:
            self.assigndriver_entry.insert(0, f"{global_variable.driver_id}")


    def assign_Driver(self):
        #get value from entry field
        booking_id = self.cus_id_entry.get()
        driver_id = self.assigndriver_entry.get()

        # Get the driver status from global_variable
        status = global_variable.driver_status
        if status != "Reserved":
            if booking_id == "" or driver_id == "":
                messagebox.showerror("ERROR", "Fill all the details.")
            else:
                # Create a Booking object
                booking = Booking(booking_id=booking_id, status="approved", driver_id=driver_id)
                assignDriver = assign_driver(booking)
                if assignDriver:
                    messagebox.showinfo("success", "Successfully Assigned Driver.")
                    self.clear()   # Clear the entry fields
                    global_variable.driver_id=0 # Reset global driver_id variable
                    global_variable.driver_status = None # Reset global driver_status variable
                    self.showtreetabel()  # Refresh the tree/table to reflect changes
                else:
                    messagebox.showerror("ERROR", f"Sorry, Cannot assign driver to the booking ID {booking_id}")
        else:
            messagebox.showerror("ERROR", "The driver is already assigned")
            self.clear()  #calling function clear()

    # Clear the entry fields
    def clear(self):
        self.cus_id_entry.delete(0, END)
        self.assigndriver_entry.delete(0, END)

if __name__ == '__main__':
    window = Tk()
    drivertable = AssignDriver(window)
    window.mainloop()