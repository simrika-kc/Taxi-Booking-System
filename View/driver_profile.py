from tkinter import *
from tkinter import messagebox
from PIL import Image as image, ImageTk
from tkinter import ttk

from Controller.driver_controll import fetchdriver_profile
from Controller.driver_register import driver_register, fetchdriver_data
from Model import global_variable
from Model.driver import Driver
from Model.global_variable import driver


class DriverProfile: #making class
    def __init__(self, window):
        self.window = window

        self.window.title("Taxi booking system")  # setting title
        self.driver_info() # calling driver_info function


    def driver_info(self):
        self.frame=Frame(self.window,width=1213,height=544,bg="#B0A695",borderwidth=1,relief="solid")
        self.frame.place(x=311,y=122)

        self.driver_label = Label(self.frame, text="Profile Information", font=("Rockwell", 25, "bold"), fg="black",bg="#B0A695")
        self.driver_label.place(x=445, y=35)

        # adding jtable
        self.column = ("Driver_ID", "full Name", "Address", "Mobile","Status")
        self.tree = ttk.Treeview(self.frame, columns=self.column, show="headings")

        for col in self.column:
            self.tree.heading(col, text=col)
        self.tree.place(x=85, y=100)
        self.showfor_table()

    def showfor_table(self):
        fortable = fetchdriver_profile()

        for row in self.tree.get_children():  #to delete the existing data
            self.tree.delete(row)

        for result in fortable:  #for inserting data in table
            self.tree.insert('', END, values=result)



if __name__ == '__main__':
    window = Tk()
    drivertable = DriverProfile(window)
    window.mainloop()