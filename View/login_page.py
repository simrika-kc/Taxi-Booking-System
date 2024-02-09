from tkinter import *
from tkinter import messagebox
from PIL import Image as image, ImageTk
from tkinter import  messagebox
from Controller.login import login_customer, login_driver, login_admin
from Model import global_variable
from Model.admin import Admin
from Model.driver import Driver
from View.admin_dash import AdminBoard
from View.dash_board import DashBoard
from View.driver_dashboard import DriverBoard
from register_page import *
from Model.customer import *
class LoginPage:
    def __init__(self, window):
        self.window = window
        
        self.window.title("Taxi booking system") #setting title
        self.window.state("zoomed")
        self.window.configure(bg="#F1EAFF") #adding background color
        self.title_label=Label(window,text="Taxi Booking System",font=("Times new roman",35,"bold"),fg="black")
        self.title_label.place(relx=0.5,rely=0.1,anchor="center")
        
        self.frame=Frame(window,width=860, height=505,bg="#E5D4FF") # making frame
        self.frame.place(x=328,y=185) #placing frame

        #adding image in frame
        self.image = image.open("Images/login_img.png")
        self.photo = ImageTk.PhotoImage(self.image)

        self.use_image=Label(self.frame,image=self.photo,bg="#E5D4FF")
        self.use_image.place(x=35,y=70)
        
        self.second_frame=Frame(self.frame,width=430,height=420,bg="#E5D4FF") #adding self.second_frame into frame
        self.second_frame.place(x=425,y=45)
        
        self.login_heading=Label(self.second_frame,text="Login",font=("Times new roman",21,"bold"),fg="black",bg="#E5D4FF")
        self.login_heading.place(relx=0.5,rely=0.15,anchor="center")
        
        #for username
        self.username_label=Label(self.second_frame,text="UserName : ",font=("Times new roman",15,""),fg="black",bg="#E5D4FF")
        self.username_label.place(x=45,y=145)
        
        self.username_entry=Entry(self.second_frame,width=16,font=("Times new roman",18,))
        self.username_entry.place(x=180,y=145)
        
        #for password
        self.password_label=Label(self.second_frame,text="Password : ",font=("Times new roman",15,""),fg="black",bg="#E5D4FF")
        self.password_label.place(x=45,y=215)
        
        self.password_entry=Entry(self.second_frame,show="*",width=16,font=("Times new roman",18,))
        self.password_entry.place(x=180,y=215)

        def login_logic():
            customer=Customer(user_name=self.username_entry.get(),password=self.password_entry.get())  #calling class name of Model.customer class
            driver=Driver(username=self.username_entry.get(),password=self.password_entry.get())  #calling class name of Model.driver class
            admin=Admin(username=self.username_entry.get(),password=self.password_entry.get())  #calling class name of Model.customer class


            loginCustomer=login_customer(customer) #making object of cass login_customer which is in controller "Login.py"
            loginDriver=login_driver(driver)   #making object of cass login_driver which is in controller "Login.py"
            loginAdmin = login_admin(admin)     #making object of cass login_admin which is in controller "Login.py"

            #using if, elif and else for validation
            if loginCustomer!=None:
                global_variable.customer=loginCustomer
                messagebox.showinfo("Welcome","Welcome to Customer Dashboard")
                self.afterlogincustomer()

            elif loginDriver!= None:
                global_variable.driver = loginDriver
                messagebox.showinfo("Welcome", "Welcome to DriverDashboard")
                self.afterlogindriver()


            elif loginAdmin!= None:
                global_variable.admin = loginAdmin
                messagebox.showinfo("Welcome", "Welcome to AdminDashboard")
                self.afterloginadmin()
            else:
                messagebox.showerror("ERROR","Invalid credintial")


        #creating login button
        self.login_button=Button(self.second_frame,text="Login",width=30,height=1,bg="#7743DB",fg="white",font=("Times new roman",15,),command=login_logic)
        self.login_button.place(x=45,y=290)
        
        #for creating new accountooo

        self.newaccount_label=Label(self.second_frame,text="Create a new account ",font=("Times new roman",14,""),fg="black",bg="#E5D4FF")
        self.newaccount_label.place(x=90,y=370)
        
        self.signup_label=Label(self.second_frame,text="Signup ",fg="#5D12D2",font=("Times new roman",13,"underline"),cursor="hand2",bg="#E5D4FF")
        self.signup_label.place(x=260,y=370)
        self.signup_label.bind("<Button-1>",self.register_page)

        #function for signup

    def register_page(self,event):
        self.frame.destroy() #to remove frame

        registerPage = RegisterPage(self.window)  #making object, making object of the register_page class

       # registerPage.registration_frame()  #to call the function we should use object name i.e. register_page


#faaking functions to use in pages
    def afterlogincustomer(self):
        self.window.destroy()
        window = Tk()
        dashboard = DashBoard(window)  # making object of the Dashboard class
        window.mainloop()

    def afterlogindriver(self):
        self.window.destroy()
        window = Tk()
        dashboard = DriverBoard(window)
        window.mainloop()

    def afterloginadmin(self):
        self.window.destroy()
        window = Tk()
        dashboard = AdminBoard(window)
        window.mainloop()



if __name__ == '__main__':
    loginpage_window = Tk()
    login_page = LoginPage(loginpage_window)
    loginpage_window.mainloop()
