from tkinter import *
from tkinter import messagebox
from PIL import Image as image, ImageTk
from tkinter import ttk

from Controller.driver_register import driver_register, fetchdriver_data
from Model import global_variable
from Model.driver import Driver
from Model.global_variable import driver


class DriverTable: #making class
    def __init__(self, window):
        self.window = window

        self.window.title("Taxi booking system")  # setting title
        self.driver_info() # calling driver_info function


    def driver_info(self):
        self.frame=Frame(self.window,width=1213,height=544,bg="#B0A695",borderwidth=1,relief="solid")
        self.frame.place(x=311,y=122)

        # for fullname
        self.fullname_label = Label(self.frame, text="fullname : ", font=("Times new roman", 15, ""), fg="black",
                                    bg="#B0A695")
        self.fullname_label.place(x=45, y=45)

        self.fullname_entry = Entry(self.frame, width=16, font=("Times new roman", 18,))
        self.fullname_entry.place(x=140, y=45)

        # for Address
        self.address_label = Label(self.frame, text="Address : ", font=("Times new roman", 15, ""), fg="black",
                                   bg="#B0A695")
        self.address_label.place(x=45, y=110)

        self.address_entry = Entry(self.frame, width=16, font=("Times new roman", 18,))
        self.address_entry.place(x=140, y=110)
        # for number
        self.number_label = Label(self.frame, text="Licence plate : ", font=("Times new roman", 15, ""), fg="black",
                                  bg="#B0A695")
        self.number_label.place(x=395, y=45)

        self.number_entry = Entry(self.frame, width=16, font=("Times new roman", 18,))
        self.number_entry.place(x=520, y=45)
        # for username
        self.username_label = Label(self.frame, text="Username : ", font=("Times new roman", 15, ""), fg="black",
                                    bg="#B0A695")
        self.username_label.place(x=393, y=110)

        self.username_Entry = Entry(self.frame, width=16, font=("Times new roman", 18,))
        self.username_Entry.place(x=495, y=110)
        # new password
        self.password_label = Label(self.frame, text="Password : ", font=("Times new roman", 15, ""), fg="black",
                                    bg="#B0A695")
        self.password_label.place(x=745, y=45)

        self.password_Entry = Entry(self.frame, width=16, font=("Times new roman", 18,))
        self.password_Entry.place(x=850, y=45)

        # confirm password field
        self.mobile_label = Label(self.frame, text="mobile : ", font=("Times new roman", 15, ""),
                                       fg="black", bg="#B0A695")
        self.mobile_label.place(x=755, y=110)

        self.mobile_Entry = Entry(self.frame, width=16, font=("Times new roman", 18,))
        self.mobile_Entry.place(x=850, y=110)

        # register button
        self.register_Button = Button(self.frame, text="Register", width=26, height=1, bg="#2E97A7", fg="white",
                                      font=("Times new roman", 15, "bold"),command=self.driver_registration)
        self.register_Button.place(x=398, y=176)


        self.driver_label = Label(self.frame, text="Driver Informations", font=("Rockwell", 25, "bold"), fg="black",bg="#B0A695")
        self.driver_label.place(x=445, y=235)


        # adding jtable
        self.column = ("Driver_ID", "full Name", "Address", "Mobile","Status")
        self.tree = ttk.Treeview(self.frame, columns=self.column, show="headings")

        for col in self.column:
            self.tree.heading(col, text=col)
        self.tree.place(x=85, y=300)
        self.tree.bind("<ButtonRelease-1>", self.select_booking)
        self.showfor_table()

    def showfor_table(self):
        # Retrieve driver data using the fetchdriver_data() function

        fortable = fetchdriver_data()

        for row in self.tree.get_children():  #to delete the existing data
            self.tree.delete(row)

        for result in fortable:  #for inserting data in table
            self.tree.insert('', END, values=result)



#for driver registration

    def driver_registration(self):

        #get value from entry fields
        fullname=self.fullname_entry.get()
        address=self.address_entry.get()
        number=self.number_entry.get()
        username=self.username_Entry.get()
        password=self.password_Entry.get()
        mobile=self.mobile_Entry.get()
 #checking if the fields are empty
        if fullname=="" or password=="" or username=="" or address=="" or number=="" or mobile=="":
            messagebox.showerror("Error","Fill all the details")

        else:
            # Create a Driver object with the provided details for registration
            driver = Driver(full_name=fullname,status="Available", address=address, licence_plate=number, username=username,password=password,mobile=mobile)
            driver_Register=driver_register(driver)

            if driver_Register==True:
                messagebox.showinfo("success","successfully registered")
                self.clear_register() #calling function clear_register()
                self.showfor_table()   # Refresh the tree/table to reflect changes

            else:
                messagebox.showerror("error","Cannot registered")
 #for clear field
    def clear_register(self):
        self.fullname_entry.delete(0, END)
        self.address_entry.delete(0, END)
        self.number_entry.delete(0, END)
        self.username_Entry.delete(0, END)
        self.password_Entry.delete(0, END)
        self.mobile_Entry.delete(0, END)

        # to select row from the table
    def select_booking(self, event):
        values = self.tree.focus()
        bookings = self.tree.item(values)

        row = bookings.get('values')
        print(row)

        global_variable.driver_id =row[0]
        global_variable.driver_status = row[4]

if __name__ == '__main__':
    window = Tk()
    drivertable = DriverTable(window)
    window.mainloop()