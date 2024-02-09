import re
from tkinter import *
from tkinter import messagebox
from PIL import Image as image, ImageTk
from tkinter import ttk
from Model.customer import *
from View.login_page import LoginPage
from Controller.customer_contoller import *

class RegisterPage: #making class
    def __init__(self, window):
        self.window = window

        self.window.title("Taxi booking system")  # setting title
        self.registration_frame() # calling function in this class so we can use its class directly in login_page.

    def registration_frame(self):  #making function
        self.frame = Frame(self.window, width=770, height=505, bg="#E5D4FF")  # making frame
        self.frame.place(x=338, y=185)  # placing frame

        self.login_heading = Label(self.frame, text="Taxi Booking Registration Form", font=("Times new roman", 20, ""), fg="black",bg="#E5D4FF")
        self.login_heading.place(relx=0.5, rely=0.15, anchor="center") #setting label in the center


# for fullname
        self.fullname_label = Label(self.frame, text="fullname : ", font=("Times new roman", 15, ""), fg="black",bg="#E5D4FF")
        self.fullname_label.place(x=45, y=145)

        self.fullname_entry = Entry(self.frame, width=16, font=("Times new roman", 18,))
        self.fullname_entry.place(x=140, y=145)



# for Address
        self.address_label = Label(self.frame, text="Address : ", font=("Times new roman", 15, ""), fg="black",bg="#E5D4FF")
        self.address_label.place(x=45, y=215)

        self.address_entry = Entry(self.frame, width=16, font=("Times new roman", 18,))
        self.address_entry.place(x=140, y=215)
#for email
        self.email_label = Label(self.frame, text="Email : ", font=("Times new roman", 15, ""), fg="black", bg="#E5D4FF")
        self.email_label.place(x=45, y=280)

        self.email_entry = Entry(self.frame, width=16, font=("Times new roman", 18,))
        self.email_entry.place(x=140, y=280)
#for number
        self.number_label = Label(self.frame, text="Number : ", font=("Times new roman", 15, ""), fg="black", bg="#E5D4FF")
        self.number_label.place(x=45, y=345)

        self.number_entry = Entry(self.frame, width=16, font=("Times new roman", 18,))
        self.number_entry.place(x=140, y=345)
#for payment
        self.payment_label = Label(self.frame, text="Payment : ", font=("Times new roman", 15, ""), fg="black", bg="#E5D4FF")
        self.payment_label.place(x=385, y=145)

        self.payment_combobox=ttk.Combobox(self.frame, width=16, font=("Times new roman", 17,))
        self.payment_combobox['values']=("Esewa"),("Cash"),("Khalti"),("Fund transfer")
        self.payment_combobox.place(x=550, y=145)
#for username
        self.username_label = Label(self.frame, text="Username : ", font=("Times new roman", 15, ""), fg="black", bg="#E5D4FF")
        self.username_label.place(x=385, y=215)

        self.username_Entry=Entry(self.frame, width=16, font=("Times new roman", 18,))
        self.username_Entry.place(x=550, y=215)
#new password
        self.password_label = Label(self.frame, text="Password : ", font=("Times new roman", 15, ""), fg="black" , bg="#E5D4FF")
        self.password_label.place(x=385, y=280)

        self.password_Entry = Entry(self.frame, width=16, font=("Times new roman", 18,))
        self.password_Entry.place(x=550, y=280)

#confirm password field
        self.conpassword_label = Label(self.frame, text="Confirm Password : ", font=("Times new roman", 15, ""), fg="black",bg="#E5D4FF")
        self.conpassword_label.place(x=385, y=345)

        self.conpassword_Entry = Entry(self.frame, width=16, font=("Times new roman", 18,))
        self.conpassword_Entry.place(x=550, y=345)

#register button
        self.register_Button=Button(self.frame,text="Register",width=30,height=1,bg="#2E97A7",fg="white",font=("Times new roman",15,"bold"),command=self.for_register)
        self.register_Button.place(x=200,y=410)


#backlogin
        self.backLogin = Label(self.frame, text="Already have an account? ", font=("Times new roman", 13, ""), fg="black",bg="#E5D4FF")
        self.backLogin.place(x=240, y=465)

        self.login=Label(self.frame,text="Login in ",fg="#5D12D2",font=("Times new roman",13,"underline"),cursor="hand2",bg="#E5D4FF")
        self.login.place(x=420,y=465)
        self.login.bind("<Button-1>",self.login_pageReturn)
#get
    def for_register(self):
        fullname=self.fullname_entry.get()
        address = self.address_entry.get()
        email=self.email_entry.get()
        number=self.number_entry.get()
        payment=self.payment_combobox.get()
        username=self.username_Entry.get()
        password=self.password_Entry.get()
        conpassword=self.conpassword_Entry.get()

#for validation
        # Validate email
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            messagebox.showerror("Error", "Invalid email format")
            return

        # Validate phone number
        if not re.match(r'^\d{10}$', number):
            messagebox.showerror("Error", "Invalid phone number format (should be 10 digits)")
            return

        if self.fullname_entry.get()=="" or self.address_entry.get()=="" or self.email_entry.get()=="" or self.number_entry.get()=="" or self.payment_combobox.get()=="" or self.username_Entry.get()=="" or self.password_Entry.get()=="":
            messagebox.showerror("Error", "Fill all the details")

        elif self.password_Entry.get()!=self.conpassword_Entry.get():
            messagebox.showerror("ERROR", "Didnt match password")

        else:
#making object of class customer from Model
            customer=Customer(full_name=fullname,address=address,email=email,phone_number=number,payment_method=payment,user_name=username,password=password)   # this customer object further use in parameters in function in registering customer
            registration=register_customer(customer)
            if registration==True:
                messagebox.showinfo("Success","Successfully registered")
                self.frame.destroy()
                loginpage = LoginPage(self.window)  # making object of loginpage class to use in this page

            else:
                messagebox.showerror("unsuccess","Sorry! unable to register")


    def login_pageReturn(self,event):
        loginpage=LoginPage(self.window) #making object of loginpage class to use in this page


if __name__ == '__main__':
    window = Tk()
    register_page = RegisterPage(window)
    window.mainloop()