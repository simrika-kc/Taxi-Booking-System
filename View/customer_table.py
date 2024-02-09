from tkinter import *
from tkinter import messagebox
from PIL import Image as image, ImageTk
from tkinter import ttk

from Controller.admin_controll import customer_table


class CustomerTable: #making class
    def __init__(self, window):
        self.window = window

        self.window.title("Taxi booking system")  # setting title
        self.customer_info() # calling driver_info function


    def customer_info(self):
        self.frame=Frame(self.window,width=1213,height=544,bg="#B0A695",borderwidth=1,relief="solid")
        self.frame.place(x=311,y=122)

        self.driver_label = Label(self.frame, text="Customers Informations", font=("Rockwell", 30, "bold"), fg="black",bg="#B0A695")
        self.driver_label.place(x=425, y=25)


        # adding jtable
        self.column = ("customer_id", "full Name", "Address", "Mobile","Email","Payment method","Username")
        self.tree = ttk.Treeview(self.frame, columns=self.column, show="headings")

        for col in self.column:
            self.tree.heading(col, text=col)
            self.tree.place(x=5, y=100)
        self.tree.column("customer_id", width=160, anchor="center")
        self.tree.column("full Name", width=160, anchor="center")
        self.tree.column("Address", width=180, anchor="center")
        self.tree.column("Mobile", width=160, anchor="center")
        self.tree.column("Email", width=180, anchor="center")
        self.tree.column("Payment method", width=180, anchor="center")
        self.tree.column("Username", width=180, anchor="center")

        self.showin_table()

    def showin_table(self):

        fortable = customer_table()
        print(fortable)

        for row in self.tree.get_children():  #to delete the existing data
            self.tree.delete(row)

        for result in fortable:  #for inserting data in table
            self.tree.insert('', END, values=result)


if __name__ == '__main__':
    window = Tk()
    drivertable = CustomerTable(window)
    window.mainloop()