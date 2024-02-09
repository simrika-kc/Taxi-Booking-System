from PIL import Image as image, ImageTk
from tkinter import ttk
from tkinter import *

from Controller.admin_controll import booking_details
from Controller.customer_booking import for_table
from Model import global_variable
from Model.booking import Booking


class BookingTable: #making class
    def __init__(self, window):
        self.window = window

        self.window.title("Taxi booking system")  # setting title
        self.booking_info() # calling driver_info function


    def booking_info(self):
        self.frame=Frame(self.window,width=1213,height=544,bg="#B0A695",borderwidth=1,relief="solid")
        self.frame.place(x=311,y=122)

        self.driver_label = Label(self.frame, text="Booking Informations", font=("Rockwell", 30, "bold"), fg="black",bg="#B0A695")
        self.driver_label.place(x=425, y=25)


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

        self.showin_table()


    def showin_table(self):

        fortable = booking_details()
        print(fortable)

        for row in self.tree.get_children():  #to delete the existing data
            self.tree.delete(row)

        for result in fortable:  #for inserting data in table
            self.tree.insert('', END, values=result)


if __name__ == '__main__':
    window = Tk()
    bookingtable = BookingTable(window)
    window.mainloop()