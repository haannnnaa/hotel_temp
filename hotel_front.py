from tkinter import *
from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox
import hotel_backend
import sqlite3
import json

#=================== table management ===================#
connection = hotel_backend.connection_check()
hotel_backend.create_table(connection)


#======================= Variables ======================#
#light colors
white = "#FFFFFF" #
topmenu_lightcolor = "#01497C"
rightmenu_lightcolor = "#014F86"
#dark colors
topmenu_darkcolor = "#012A4A"
rightmenu_darkcolor = "#013A63"
dark_bg = "#1e2c3e"

dark_gray = "#AEB7B3" #
light_gray = "#b8c1bd" #
black = "#000411" #
dark_Blue = "#160C28" #
light_blue = "#1e1038" #
dark_yellow = "#EFCB68" #
light_yellow = "#f1d17a" #
#fonts
yekan = "B yekan"
iransans = "IRANSansDN"

def top_menu(root, controller):
    top_menu = Frame(root, bg= dark_Blue)
    top_menu.pack(side= 'top', fill= 'x')
    reception_b = Button(top_menu, text= 'صفحه اصلی', font=(yekan, 18, 'bold'), bg=dark_Blue, fg=white, highlightthickness=2, border=0,highlightbackground=light_blue, highlightcolor=light_blue, activebackground=light_blue, activeforeground=white, width=10, cursor='hand2', command=lambda: controller.show_frame("MainPage"))
    reception_b.pack(side= 'right', ipadx= 10, padx= 15)
    reception_b = Button(top_menu, text= 'امور پذیرش', font=(yekan, 18, 'bold'), bg=dark_Blue, fg=white, highlightthickness=2, border=0,highlightbackground=light_blue, highlightcolor=light_blue, activebackground=light_blue, activeforeground=white, width=10, cursor='hand2', command=lambda: controller.show_frame("ReceptionPage"))
    reception_b.pack(side= 'right', ipadx= 10, padx= 15)
    finance_b = Button(top_menu, text= 'امور مالی', font=(yekan, 18, 'bold'), bg=dark_Blue, fg=white, highlightthickness=2, border=0,highlightbackground=light_blue, highlightcolor=light_blue, activebackground=light_blue, activeforeground=white, width=10, cursor= 'hand2', command=lambda: controller.show_frame("PaymentPage"))
    finance_b.pack(side= 'right', ipadx= 10, padx= 15)
    Settings_b = Button(top_menu, text= 'تنظیمات', font=(yekan, 18, 'bold'), bg=dark_Blue, fg=white, highlightthickness=2, border=0,highlightbackground=light_blue, highlightcolor=light_blue, activebackground=light_blue, activeforeground=white, width=10, cursor= 'hand2', command=lambda: controller.show_frame("SettingsPage"))
    Settings_b.pack(side= 'right', ipadx= 10, padx= 15)

class HotelApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.geometry("1600x900")
        self.minsize(1600,900)     
        self.state("zoomed")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
       

        self.frames = {}
        for F in (RegisterPage, LoginPage, MainPage, SettingsPage, ReceptionPage, PaymentPage, SearchPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("RegisterPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


        

class RegisterPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        #=================== background image ===================#
        self.login_bg_img = PhotoImage(file="img/login_bg.png")
        self.login_bg_lbl = Label(self, image=self.login_bg_img)
        self.login_bg_lbl.place(y=0,x=0, relwidth=1, relheight=1)

        #=================== register frame ===================#
        self.reg_frame = Frame(self,bg=white)
        self.reg_frame.pack(expand=True, ipady=50, ipadx=250)

        #=================== Labels ===================#
        Label(self.reg_frame,text="ثبت اطلاعات برای اولین ورود",font=(iransans,22),justify="right",bg=white).place(relx=0.75, rely=0.10, anchor=N)
        
        self.reg_banner = PhotoImage(file="img/login_banner.png")
        self.banner_lbl = Label(self.reg_frame,image=self.reg_banner, bg=white)
        self.banner_lbl.pack(side=LEFT) 

        Label(self.reg_frame,text=":نام هتل",font=(yekan,14),justify="right",bg=white).place(relx=0.90, rely=0.30, anchor=N)
        Label(self.reg_frame,text=":نام کاربری",font=(yekan,14),justify="right",bg=white).place(relx=0.90, rely=0.40, anchor=N)
        Label(self.reg_frame,text=":گذرواژه",font=(yekan,14),justify="right",bg=white).place(relx=0.90, rely=0.50, anchor=N)
        Label(self.reg_frame,text=":تکرار گذرواژه",font=(yekan,14),justify="right",bg=white).place(relx=0.90, rely=0.60, anchor=N)

        #=================== Entrys ===================#
        self.hotelname_ent = ttk.Entry(self.reg_frame,font=(yekan,12),justify="center",width=25)     
        self.hotelname_ent.place(relx=0.70, rely=0.30, anchor=N)
        self.username_ent = ttk.Entry(self.reg_frame,font=(yekan,12),justify="center",width=25)
        self.username_ent.place(relx=0.70, rely=0.40, anchor=N)
        self.password_ent = ttk.Entry(self.reg_frame,font=(yekan,12),justify="center",width=25,show="*")
        self.password_ent.place(relx=0.70, rely=0.50, anchor=N)
        self.retype_password_ent = ttk.Entry(self.reg_frame,font=(yekan,12),justify="center",width=25,show="*")
        self.retype_password_ent.place(relx=0.70, rely=0.60, anchor=N)

        #=================== show and hide password function ===================#
        self.showpassword = False
        def show_password():
            if self.showpassword == False:
                self.show_password_btn.config(image=self.hide_password_img)
                self.password_ent.config(show="")
                self.retype_password_ent.config(show="")
                self.showpassword = True
            elif self.showpassword == True:
                self.show_password_btn.config(image=self.show_password_img)
                self.password_ent.config(show="*")
                self.retype_password_ent.config(show="*")
                self.showpassword = False
        
        #=================== hide and show password button ===================#
        self.show_password_img = PhotoImage(file="img/showpassword.png")
        self.hide_password_img = PhotoImage(file="img/hidepassword.png")
        self.show_password_btn = Button(self.reg_frame,width=15,
                                bg=white,
                                border=0,
                                image=self.show_password_img,
                                cursor="hand2",
                                activebackground=white,
                                command=show_password)
        self.show_password_btn.place(relx=0.57, rely=0.51, anchor=N)

        #=================== register button ===================#
        self.reg_btn = Button(self.reg_frame, text="  ثبت اطلاعات و ورود  ",font=(iransans,12),
                         bg=dark_yellow,border=0,fg=black,
                         cursor="hand2",
                         activebackground=light_yellow,
                         command=self.check_reg_data)
        self.reg_btn.place(relx=0.80, rely=0.75, anchor=N)
        
        self.reg_login_btn = Button(self.reg_frame, text="   ورود   ",font=(iransans,12),
                         bg=dark_yellow,border=0,fg=black,
                         cursor="hand2",
                         activebackground=light_yellow,
                         command=lambda: controller.show_frame("LoginPage"))
        self.reg_login_btn.place(relx=0.60, rely=0.75, anchor=N)

        self.reg_login_btn = Button(self.reg_frame, text="  تنظیمات(تست)  ",font=(iransans,12),
                         bg=dark_yellow,border=0,fg=black,
                         cursor="hand2",
                         activebackground=light_yellow,
                         command=lambda: controller.show_frame("SettingsPage"))
        self.reg_login_btn.place(relx=0.40, rely=0.75, anchor=N)

        self.reg_login_btn = Button(self.reg_frame, text="  صفحه اصلی(تست)  ",font=(iransans,12),
                         bg=dark_yellow,border=0,fg=black,
                         cursor="hand2",
                         activebackground=light_yellow,
                         command=lambda: controller.show_frame("MainPage"))
        self.reg_login_btn.place(relx=0.20, rely=0.75, anchor=N)
        
    #=================== check entrys data and save data ===================#
    def check_reg_data(self):
        
        if not(self.hotelname_ent.get()) or not(self.username_ent.get()) or not(self.password_ent.get()) or not(self.retype_password_ent.get()):
            if not(self.hotelname_ent.get()):
                self.hotelanem_ent_error = Label(self.reg_frame,text="نمیتواند خالی باشد",fg="red",bg=white,font=(yekan,10))
                self.hotelanem_ent_error.place(relx=0.53, rely=0.30, anchor=N)
                self.hotelanem_ent_error.after(3000,self.hotelanem_ent_error.destroy)

            if not(self.username_ent.get()):
                self.username_ent_error = Label(self.reg_frame,text="نمیتواند خالی باشد",fg="red",bg=white,font=(yekan,10))
                self.username_ent_error.place(relx=0.53, rely=0.40, anchor=N)
                self.username_ent_error.after(3000,self.username_ent_error.destroy)

            if not(self.password_ent.get()):
                self.password_ent_error = Label(self.reg_frame,text="نمیتواند خالی باشد",fg="red",bg=white,font=(yekan,10))
                self.password_ent_error.place(relx=0.53, rely=0.50, anchor=N)
                self.password_ent_error.after(3000,self.password_ent_error.destroy)

            if not(self.retype_password_ent.get()):
                self.retype_password_ent_error = Label(self.reg_frame,text="نمیتواند خالی باشد",fg="red",bg=white,font=(yekan,10))
                self.retype_password_ent_error.place(relx=0.53, rely=0.60, anchor=N)
                self.retype_password_ent_error.after(3000,self.retype_password_ent_error.destroy)
        
        #=================== check passwords ===================#
        elif self.password_ent.get() != self.retype_password_ent.get():
            messagebox.showerror(title="خطا",message="گذرواژه وارد شده با تکرار آن یکسان نیست")
            self.password_ent.delete(0, END)
            self.retype_password_ent.delete(0, END)

        else:
            hotel_name = self.hotelname_ent.get()
            username = self.username_ent.get()
            password = self.password_ent.get()

            try:
                #=================== save data ===================#
                connection = hotel_backend.connection_check()
                hotel_backend.add_user(connection, username, password, hotel_name)

                #=================== change frame ===================#
                self.controller.show_frame("MainPage")
                
            except sqlite3.IntegrityError :
                messagebox.showerror(title="خطا",message="این نام کاربری قبلا استفاده شده")
                self.username_ent.delete(0, END)



class LoginPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        
        #=================== background image ===================#
        self.login_bg_img = PhotoImage(file="img/login_bg.png")
        self.login_bg_lbl = Label(self, image=self.login_bg_img)
        self.login_bg_lbl.place(y=0,x=0, relwidth=1, relheight=1)

        #=================== register frame ===================#
        self.login_frame = Frame(self,bg=white)
        self.login_frame.pack(expand=True, ipady=50, ipadx=250)

        #=================== Labels ===================#
        Label(self.login_frame,text="ورود به برنامه",font=(iransans,22),justify="right",bg=white).place(relx=0.80, rely=0.20, anchor=N)
        
        self.login_banner = PhotoImage(file="img/login_banner.png")
        self.banner_lbl = Label(self.login_frame,image=self.login_banner, bg=white)
        self.banner_lbl.pack(side=LEFT) 

        Label(self.login_frame,text=":نام کاربری",font=(yekan,14),justify="right",bg=white).place(relx=0.90, rely=0.40, anchor=N)
        Label(self.login_frame,text=":گذرواژه",font=(yekan,14),justify="right",bg=white).place(relx=0.90, rely=0.50, anchor=N)

        #=================== Entrys ===================#
        self.username_ent = ttk.Entry(self.login_frame,font=(yekan,12),justify="center",width=25)
        self.username_ent.place(relx=0.70, rely=0.40, anchor=N)
        self.password_ent = ttk.Entry(self.login_frame,font=(yekan,12),justify="center",width=25,show="*")
        self.password_ent.place(relx=0.70, rely=0.50, anchor=N)

        #=================== show and hide password function ===================#
        self.showpassword = False
        def show_password():
            if self.showpassword == False:
                self.show_password_btn.config(image=self.hide_password_img)
                self.password_ent.config(show="")
                self.showpassword = True
            elif self.showpassword == True:
                self.show_password_btn.config(image=self.show_password_img)
                self.password_ent.config(show="*")
                self.showpassword = False
        
        #=================== hide and show password button ===================#
        self.show_password_img = PhotoImage(file="img/showpassword.png")
        self.hide_password_img = PhotoImage(file="img/hidepassword.png")
        self.show_password_btn = Button(self.login_frame,width=15,
                                bg=white,
                                border=0,
                                image=self.show_password_img,
                                cursor="hand2",
                                activebackground=white,
                                command=show_password)
        self.show_password_btn.place(relx=0.57, rely=0.51, anchor=N)

        #=================== login button ===================#
        self.reg_btn = Button(self.login_frame, text="  ورود   ",font=(iransans,12),
                         bg=dark_yellow,border=0,fg=black,
                         cursor="hand2",
                         activebackground=light_yellow,
                         command=self.check_login_data)
        self.reg_btn.place(relx=0.70, rely=0.70, anchor=N)
    #=================== check entrys data ===================#
    def check_login_data(self):

        if not (self.username_ent.get()) or not (self.password_ent.get()):
            if not (self.username_ent.get()):
                self.username_ent_error = Label(self.login_frame,text="نمیتواند خالی باشد",fg="red",bg=white,font=(yekan,10))
                self.username_ent_error.place(relx=0.53, rely=0.40, anchor=N)
                self.username_ent_error.after(3000,self.username_ent_error.destroy)

            if not (self.password_ent.get()):
                self.password_ent_error = Label(self.login_frame,text="نمیتواند خالی باشد",fg="red",bg=white,font=(yekan,10))
                self.password_ent_error.place(relx=0.53, rely=0.50, anchor=N)
                self.password_ent_error.after(3000,self.password_ent_error.destroy)

        #=================== error wrong username/password ===================#
        else : 
            username = self.username_ent.get()
            password = self.password_ent.get()
            connection = hotel_backend.connection_check()
            user_info = hotel_backend.select_login(connection, username, password)
            if [(username, password)] != user_info :
                messagebox.showerror(title="خطا",message="نام کاربری یا گذرواژه وارده شده اشتباه است")
                self.username_ent.delete(0, END)
                self.password_ent.delete(0, END)

        #=================== Change frame ===================#    
            elif [(username, password)] == user_info :
                self.controller.show_frame("MainPage")
                self.username_ent.delete(0, END)
                self.password_ent.delete(0, END)
    

class MainPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg=white)

        self.darkmode_var = False
        def darkmode_function():
            if self.darkmode_var == False:
                #main page bg
                self.config(bg=dark_bg)
                #top menu
                top_menu.config(bg=topmenu_darkcolor)
                reception_b.config(bg=topmenu_darkcolor)
                reception_bb.config(bg=topmenu_darkcolor)
                finance_b.config(bg=topmenu_darkcolor)
                Settings_b.config(bg=topmenu_darkcolor)
                self.logout_btn.config(bg=topmenu_darkcolor)
                self.darkmode_btn.config(bg=topmenu_darkcolor)
                #countdata frame
                self.mp_hotelname.config(bg=dark_bg, fg=white)
                self.allrooms.config(bg=dark_bg, fg=white)
                self.allclients.config(bg=dark_bg, fg=white)
                self.emptyrooms.config(bg=dark_bg, fg=white)


                self.darkmode_var = True
            elif self.darkmode_var == True:
                #main page bg
                self.config(bg=white)
                #top menu
                top_menu.config(bg=topmenu_lightcolor)
                reception_b.config(bg=topmenu_lightcolor)
                reception_bb.config(bg=topmenu_lightcolor)
                finance_b.config(bg=topmenu_lightcolor)
                Settings_b.config(bg=topmenu_lightcolor)
                self.logout_btn.config(bg=topmenu_lightcolor)
                self.darkmode_btn.config(bg=topmenu_lightcolor)
                #countdata frame
                self.mp_hotelname.config(bg=white, fg="black")
                self.allrooms.config(bg=white, fg="black")
                self.allclients.config(bg=white, fg="black")
                self.emptyrooms.config(bg=white, fg="black")
                self.darkmode_var = False



        #=================== Top Menu ===================#
        top_menu = Frame(self, bg= topmenu_lightcolor)
        top_menu.pack(side= 'top', fill= 'x')
        reception_b = Button(top_menu, text= 'صفحه اصلی', font=(yekan, 18, 'bold'), bg=topmenu_lightcolor, fg=white, highlightthickness=2, border=0,highlightbackground=light_blue, highlightcolor=light_blue, activebackground=topmenu_lightcolor, activeforeground=white, width=10, cursor='hand2', command=lambda: controller.show_frame("MainPage"))
        reception_b.pack(side= 'right', ipadx= 10, padx= 15)
        reception_bb = Button(top_menu, text= 'امور پذیرش', font=(yekan, 18, 'bold'), bg=topmenu_lightcolor, fg=white, highlightthickness=2, border=0,highlightbackground=light_blue, highlightcolor=light_blue, activebackground=topmenu_lightcolor, activeforeground=white, width=10, cursor='hand2', command=lambda: controller.show_frame("ReceptionPage"))
        reception_bb.pack(side= 'right', ipadx= 10, padx= 15)
        finance_b = Button(top_menu, text= 'امور مالی', font=(yekan, 18, 'bold'), bg=topmenu_lightcolor, fg=white, highlightthickness=2, border=0,highlightbackground=light_blue, highlightcolor=light_blue, activebackground=topmenu_lightcolor, activeforeground=white, width=10, cursor= 'hand2', command=lambda: controller.show_frame("PaymentPage"))
        finance_b.pack(side= 'right', ipadx= 10, padx= 15)
        Settings_b = Button(top_menu, text= 'تنظیمات', font=(yekan, 18, 'bold'), bg=topmenu_lightcolor, fg=white, highlightthickness=2, border=0,highlightbackground=light_blue, highlightcolor=light_blue, activebackground=topmenu_lightcolor, activeforeground=white, width=10, cursor= 'hand2', command=lambda: controller.show_frame("SettingsPage"))
        Settings_b.pack(side= 'right', ipadx= 10, padx= 15)

        #logout button
        self.logout_img = PhotoImage(file="icons/logout.png")
        self.logout_btn = Button(top_menu, image=self.logout_img, bg=topmenu_lightcolor, cursor="hand2", border=0, command=lambda: controller.show_frame("LoginPage"))
        self.logout_btn.pack(side="left", padx=20)

        #darkmode button
        self.moon_img = PhotoImage(file="icons/moon.png")
        self.sun_img = PhotoImage(file="icons/sun.png")
        self.darkmode_btn = Button(top_menu, image=self.moon_img, bg=topmenu_lightcolor, cursor="hand2", border=0, command=darkmode_function)
        self.darkmode_btn.pack(side="left", padx=20)



        with open("config.json","r", encoding="utf-8") as configFile:
            configdata = json.load(configFile)

        self.hotel_name = configdata["hotelname"]
        
        self.mp_hotelname = Label(self, text=self.hotel_name, font=(yekan, 23))
        self.mp_hotelname.pack(pady=30)

        countdata = Frame(self)
        countdata.pack(expand=True)

        self.allrooms = Label(countdata, text=":تعداد کل اتاق  ها",font=(yekan, 18))
        self.allrooms.pack(side="right",padx=30)
        self.allclients = Label(countdata, text=":تعداد کل مهمان ها",font=(yekan, 18))
        self.allclients.pack(side="right",padx=30)
        self.emptyrooms =  Label(countdata, text=":اتاق های خالی",font=(yekan, 18))
        self.emptyrooms.pack(side="right",padx=30)




class SettingsPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        top_menu(self, controller)

        self.right_menu = Frame(self, bg= dark_gray)
        self.right_menu.pack(side="right",fill="y")

        label_r = Label(self.right_menu, text="Right Menu", font=controller)
        label_r.pack(pady=30)


        #read json file data
        with open("config.json","r", encoding="utf-8") as configFile:
            configdata = json.load(configFile)
            settings_hotelname = configdata["hotelname"]
            # settings_username = configdata["username"]
            settings_password = configdata["password"]

        
        #=================== Change hotelname and admin username ===================#
        Label(self,text=":نام هتل", font=(yekan,14)).place(relx=0.70, rely=0.20)
        setting_hotelname_ent = ttk.Entry(self,font=(yekan,12),justify="right")
        setting_hotelname_ent.insert(0, settings_hotelname)
        setting_hotelname_ent.place(relx=0.57, rely=0.20)  

        # Label(self,text=":نام کاربری", font=(yekan,14)).place(relx=0.70, rely=0.25)
        # setting_user_ent = ttk.Entry(self,font=(yekan,12),justify="left")
        # setting_user_ent.insert(0, settings_username)
        # setting_user_ent.place(relx=0.57, rely=0.25)

        self.change_admininfo_btn = Button(self, text="  تغییر اطلاعات  ",font=(iransans,12),
                            bg=dark_yellow,border=0,fg=black,
                            cursor="hand2",
                            activebackground=light_yellow)
        self.change_admininfo_btn.place(relx=0.60, rely=0.30)


        #=================== Change admin password ===================#
        #check box
        self.admin_pass_cb = False
        def change_admin_pass():
            if self.admin_pass_cb == False:
                self.setting_current_pass_ent.config(state="normal")
                self.setting_new_pass_ent.config(state="normal")
                self.setting_renew_pass_ent.config(state="normal")
                self.setting_current_pass_ent.delete(0, END)
                self.setting_new_pass_ent.delete(0, END)
                self.setting_renew_pass_ent.delete(0, END)
                self.change_adminpass_btn.config(state="normal")
                self.admin_pass_cb = True
            else:
                self.setting_current_pass_ent.config(state="disabled")
                self.setting_new_pass_ent.config(state="disabled")
                self.setting_renew_pass_ent.config(state="disabled")
                self.change_adminpass_btn.config(state="disabled")
                self.admin_pass_cb = False

        #change admin password
        def change_pass():
            if self.setting_current_pass_ent.get() != settings_password :
                messagebox.showerror(title="خطا",message="رمزعبور فعلی اشتباه است")
                self.setting_current_pass_ent.delete(0, END)
                self.setting_new_pass_ent.delete(0, END)
                self.setting_renew_pass_ent.delete(0, END)
            
            if self.setting_new_pass_ent.get() != self.setting_renew_pass_ent.get():
                messagebox.showerror(title="خطا",message="رمزعبور جدید با تکرار آن یکسان نیست")
                self.setting_current_pass_ent.delete(0, END)
                self.setting_new_pass_ent.delete(0, END)
                self.setting_renew_pass_ent.delete(0, END)
            
            if self.setting_current_pass_ent.get() == settings_password and self.setting_new_pass_ent.get() == self.setting_renew_pass_ent.get() and self.setting_new_pass_ent.get() and self.setting_renew_pass_ent.get() :
                messagebox.showinfo(title="انجام شد",message="رمزعبور با موفقیت تغییر کرد")
                
                #read json file data
                with open("config.json","r", encoding="utf-8") as configFile:
                    configdata = json.load(configFile)

                    configdata["password"] = self.setting_new_pass_ent.get()

                #write data 
                with open("config.json","w", encoding="utf-8") as configFile:
                    json.dump(configdata, configFile, ensure_ascii=False)

                self.setting_current_pass_ent.delete(0, END)
                self.setting_new_pass_ent.delete(0, END)
                self.setting_renew_pass_ent.delete(0, END)


        self.change_pass = Checkbutton(self,text="تغییر رمزعبور",font=(yekan,12), command=change_admin_pass)
        self.change_pass.place(relx=0.70, rely=0.46)

        Label(self,text=":رمزعبور فعلی", font=(yekan,14)).place(relx=0.70, rely=0.50)
        self.setting_current_pass_ent = ttk.Entry(self,font=(yekan,12),justify="left",state="disabled")
        self.setting_current_pass_ent.place(relx=0.57, rely=0.50)

        Label(self,text=":رمزعبور جدید", font=(yekan,14)).place(relx=0.70, rely=0.55)
        self.setting_new_pass_ent = ttk.Entry(self,font=(yekan,12),justify="left",state="disabled")
        self.setting_new_pass_ent.place(relx=0.57, rely=0.55)

        Label(self,text=":تکرار رمزعبور جدید", font=(yekan,14)).place(relx=0.70, rely=0.60)
        self.setting_renew_pass_ent = ttk.Entry(self,font=(yekan,12),justify="left",state="disabled")
        self.setting_renew_pass_ent.place(relx=0.57, rely=0.60)
        
        self.change_adminpass_btn = Button(self, text="  تغییر رمز  ",font=(iransans,12),
                            bg=dark_yellow,border=0,fg=black,
                            cursor="hand2",
                            activebackground= light_yellow,
                            state="disabled",
                            command=change_pass)
        self.change_adminpass_btn.place(relx=0.60, rely=0.70)
   
class ReceptionPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        top_menu(self, controller)

        self.guests_side_page = Frame(self, bg= dark_gray)
        self.guests_side_page.pack(side= 'right', fill= Y)

        self.reception_button = Button(self.guests_side_page, text= 'پذیرش مهمان', font=(yekan, 12, 'bold'), bg=dark_gray, fg=black, highlightthickness=2, border=0, highlightbackground=light_gray, highlightcolor=white, activebackground=light_gray, activeforeground=black, width=10, cursor= 'hand2', command=lambda: controller.show_frame('ReceptionPage'))
        self.reception_button.pack(side= 'top', pady= 15)

        self.search_button = Button(self.guests_side_page, text= 'جستجوی مهمان', font=(yekan,12, 'bold'),bg=dark_gray, fg=black, highlightthickness=2, border=0, highlightbackground=light_gray, highlightcolor=white, activebackground=light_gray, activeforeground=black, width=10, cursor= 'hand2', command=lambda: controller.show_frame("SearchPage"))
        self.search_button.pack(side= 'top', pady= 15)

        self.reception_page  = Frame(self, bg= 'white')
        self.reception_page.pack(fill= 'both', expand= True)

        self.reception_l = Label(self.reception_page, text= 'پذیرش مهمان', font=(yekan, 30), bg= 'white')
        self.reception_l.pack(side= 'top')

        #======chaging tree view style=========#
        tvstyle = ttk.Style(self.reception_page)

        #=changing selected tree view row color=#
        tvstyle.map('Treeview', background=[('selected', light_blue)])

        tvstyle.configure("Trstyle.Treeview.Heading", foreground='black', font=(yekan, 15,'bold'), selectmode='browse' )
        self.reception_tv = ttk.Treeview(self.reception_page, style="Trstyle.Treeview")
        self.reception_tv.place(x=140, y=90)
        self.reception_tv["columns"]=('guest_id','phone_number','nationality','gender','id', 'lastname', 'name', 'row')

        self.tv_scroll = ttk.Scrollbar(self.reception_page, orient ="vertical", command=self.reception_tv.yview)
        self.tv_scroll.place(x=141, y=91, height=229)
        self.reception_tv.configure(yscrollcommand=self.tv_scroll.set)

        self.reception_tv.heading('guest_id', text='شماره پذیرش')
        self.reception_tv.heading('phone_number', text='شماره تماس')
        self.reception_tv.heading('nationality', text='ملیت')
        self.reception_tv.heading('gender', text='جنسیت')
        self.reception_tv.heading('id', text='کد ملی')
        self.reception_tv.heading('lastname', text= 'نام خانوادگی')
        self.reception_tv.heading('name', text= 'نام')
        self.reception_tv.heading('row', text='ردیف')

        self.reception_tv.column('guest_id', width=150, anchor="c",minwidth= 60)
        self.reception_tv.column('phone_number', width=150, anchor="c",minwidth= 60)
        self.reception_tv.column('nationality', width=80, anchor="c", minwidth= 60)
        self.reception_tv.column('gender', width=80, anchor="c", minwidth= 70)
        self.reception_tv.column('id', width=150, anchor="c", minwidth= 75)
        self.reception_tv.column('lastname', width=150, anchor="c", minwidth= 120)
        self.reception_tv.column('name', width=150, anchor="c", minwidth= 60)
        self.reception_tv.column('row', width=60, anchor="c", minwidth= 60)


        # changing row color by the tag given to the inserted items in the tree view
        self.reception_tv.tag_configure('oddrow', background='#c9d3e6')
        self.reception_tv.tag_configure('evenrow', background= '#e5eaf2')

        # labels
        self.name_l = Label(self.reception_page, text= 'نام', font=(yekan,20), background= 'white')
        self.name_l.place(x=1235, y=350)

        self.name_e = ttk.Entry(self.reception_page, font= (yekan, 10), justify="center", width= 20)
        self.name_e.place(x= 1035, y= 365)

        self.id_l = Label(self.reception_page, text= 'کد ملی', font=(yekan,20), background= 'white')
        self.id_l.place(x= 835, y=350)

        self.id_e = ttk.Entry(self.reception_page, font= (yekan, 10), justify="center", width= 20)
        self.id_e.place(x= 635, y= 365)

        self.gender_l = Label(self.reception_page, text= 'جنسیت', font=(yekan,20), background= 'white')
        self.gender_l.place(x= 430, y=350)
        

        self.gender_e = ttk.Combobox(self.reception_page, values= ['مرد', 'زن'], font= (yekan, 10, 'bold'), justify='center', width= 18)
        self.gender_e.place(x=215, y= 365)
        

        self.lastname_l = Label(self.reception_page, text= 'نام خانوادگی', font=(yekan,18), background= 'white')
        self.lastname_l.place(x=1225, y=450)

        self.lastname_e = ttk.Entry(self.reception_page, font= (yekan, 10), justify="center", width= 20)
        self.lastname_e.place(x=1035, y= 465 )

        self.phone_number_l = Label(self.reception_page, text= 'شماره تماس', font=(yekan,18), background= 'white')
        self.phone_number_l.place(x=825, y=450)

        self.phone_number_e = ttk.Entry(self.reception_page, font= (yekan, 10), justify="center", width= 20)
        self.phone_number_e.place(x= 635 , y=465)

        self.nationality_l = Label(self.reception_page, text= 'ملیت', font=(yekan,20), background= 'white')
        self.nationality_l.place(x= 465 , y=450)

        self.nationality_e = ttk.Combobox(self.reception_page, values= ['غیر ایرانی', 'ایرانی'], font= (yekan, 10, 'bold'), justify='center', width= 18)
        self.nationality_e.place(x= 215 , y=465)

        self.register_button = Button(self.reception_page, text= 'ثبت اطلاعات', font= (yekan, 15), bg=dark_yellow, fg=black, highlightthickness=2, border=0,highlightbackground=light_yellow, highlightcolor=light_yellow, activebackground=light_yellow, activeforeground=black,width= 15, cursor= 'hand2', command= self.check_data)
        self.register_button.place(relx= 0.43, rely= 0.8)

        self.show_items_treeview()

    def show_items_treeview(self):
        #======================select all the items in the table===================#
        all_guests = hotel_backend.show_guests(connection,7)

        #=====================Clear the treeview list items========================#
        for item in self.reception_tv.get_children():
            self.reception_tv.delete(item)
        self.row = 0

        #=========inseert all the items in the "guest_tbl" table to treeView=======#
        for listTuples in all_guests:
            self.row += 1
            if self.row % 2 == 0 :
                self.reception_tv.insert("","end", values=(listTuples[0], listTuples[6], listTuples[5], listTuples[4], listTuples[3], listTuples[2], listTuples[1], self.row), tags = ('evenrow',))
            else :
                self.reception_tv.insert("","end", values=(listTuples[0], listTuples[6], listTuples[5], listTuples[4], listTuples[3], listTuples[2], listTuples[1], self.row), tags = ('oddrow',))

        

    def check_data(self):
        correctness = True
        #====================checking the entered data by the user==========================#
        if not(self.name_e.get()) or not(self.id_e.get())or not(self.gender_e.get()) or not(self.lastname_e.get()) or not(self.phone_number_e.get()) or not(self.nationality_e.get()) :
            correctness = False
            self.error = Label(self.reception_page, text=" لطفا همهء موارد فوق را پر کنید",fg="red",bg=white,font=(yekan,10))
            self.error.place(relx= 0.445, rely=0.9)
            self.error.after(3000,self.error.destroy)

        if not(self.name_e.get()) :
            self.error = Label(self.reception_page, text='*',fg="red",bg=white,font=(yekan,20))
            self.error.place(x= 1000, y= 358)
            self.error.after(3000,self.error.destroy)
        elif not (self.name_e.get()).isalpha() :
            correctness = False
            self.error = Label(self.reception_page, text='فقط به حروف',fg="red",bg=white,font=(yekan,12))
            self.error.place(x= 1115, y= 400)
            self.error.after(3000,self.error.destroy)

        if not(self.id_e.get()) :
            self.error = Label(self.reception_page, text='*',fg="red",bg=white,font=(yekan,20))
            self.error.place(x= 600, y= 358)
            self.error.after(3000,self.error.destroy)
        elif not (self.id_e.get()).isnumeric():
            correctness = False
            self.error = Label(self.reception_page, text='فقط به عدد',fg="red",bg=white,font=(yekan,12))
            self.error.place(x= 730, y= 400)
            self.error.after(3000,self.error.destroy)
        elif len(self.id_e.get()) > 9 or len(self.id_e.get()) < 9:
            correctness = False
            self.error = Label(self.reception_page, text='فقط عدد نه رقمی ',fg="red",bg=white,font=(yekan,12))
            self.error.place(x= 695, y= 400)
            self.error.after(3000,self.error.destroy)
        

        if not(self.gender_e.get()) :
            self.error = Label(self.reception_page, text='*',fg="red",bg=white,font=(yekan,20))
            self.error.place(x= 170, y= 358)
            self.error.after(3000,self.error.destroy)
        elif not (self.gender_e.get())  == 'مرد'and not (self.gender_e.get())  == 'زن':
            correctness = False
            self.error = Label(self.reception_page, text='فقط گذینه های مشخص شده',fg="red",bg=white,font=(yekan,12))
            self.error.place(x= 230, y= 400)
            self.error.after(3000,self.error.destroy)
        
        if not(self.lastname_e.get()) :
            self.error = Label(self.reception_page, text='*',fg="red",bg=white,font=(yekan,20))
            self.error.place(x=1000, y= 460)
            self.error.after(3000,self.error.destroy)
        elif not (self.lastname_e.get()).isalpha() :
            correctness = False
            self.error = Label(self.reception_page, text='فقط به حروف',fg="red",bg=white,font=(yekan,12))
            self.error.place(x= 1115, y= 500)
            self.error.after(3000,self.error.destroy)
            
        if not(self.phone_number_e.get()) :
            self.error = Label(self.reception_page, text='*',fg="red",bg=white,font=(yekan,20))
            self.error.place(x=600, y= 460)
            self.error.after(3000,self.error.destroy)

        if not(self.nationality_e.get()) :
            self.error = Label(self.reception_page, text='*',fg="red",bg=white,font=(yekan,20))
            self.error.place(x= 170, y= 460)
            self.error.after(3000,self.error.destroy)
        elif not (self.nationality_e.get())  == 'ایرانی'and not (self.nationality_e.get())  == 'غیر ایرانی':
            correctness = False
            self.error = Label(self.reception_page, text='فقط گذینه های مشخص شده',fg="red",bg=white,font=(yekan,12))
            self.error.place(x= 230, y= 500)
            self.error.after(3000,self.error.destroy)

        
        if correctness:
            #================adding new guest to the geust_tbl table====================#
            name = self.name_e.get()
            lastname = self.lastname_e.get()
            national_id = int(self.id_e.get())
            gender = self.gender_e.get()
            nationality = self.nationality_e.get()
            phone_number = self.phone_number_e.get()

            connection = hotel_backend.connection_check()
            all_guests = hotel_backend.show_guests(connection,6)

            for guest in all_guests :
                if guest == ((name, lastname, national_id, gender, nationality, phone_number)):
                    messagebox.showerror(title="خطا",message="اطلاعات این شخص قبلا ثبت شده")
                    break
            else:
                hotel_backend.add_guest(connection, name, lastname, national_id, gender, nationality, phone_number)
                self.show_items_treeview()

class SearchPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        top_menu(self, controller)

        self.guests_side_page = Frame(self, bg= dark_gray)
        self.guests_side_page.pack(side= 'right', fill= Y)

        self.reception_button = Button(self.guests_side_page, text= 'پذیرش مهمان', font=(yekan, 12, 'bold'), bg=dark_gray, fg=black, highlightthickness=2, border=0, highlightbackground=light_gray, highlightcolor=white, activebackground=light_gray, activeforeground=black, width=10, cursor= 'hand2', command=lambda: controller.show_frame('ReceptionPage'))
        self.reception_button.pack(side= 'top', pady= 15)

        self.search_button = Button(self.guests_side_page, text= 'جستجوی مهمان', font=(yekan,12, 'bold'),bg=dark_gray, fg=black, highlightthickness=2, border=0, highlightbackground=light_gray, highlightcolor=white, activebackground=light_gray, activeforeground=black, width=10, cursor= 'hand2', command=lambda: controller.show_frame("SearchPage"))
        self.search_button.pack(side= 'top', pady= 15)


        self.search_page  = Frame(self, bg= 'white')
        self.search_page.pack(side= 'right', fill= 'both', expand= True)

        self.reception_l = Label(self.search_page, text= 'جستجوی مهمان', font=(yekan, 30, 'bold'), bg= 'white')
        self.reception_l.pack(side= 'top')

                # chaging tree view style
        tvstyle = ttk.Style(self.search_page)

        # changing selected tree view row color
        tvstyle.map('Treeview', background=[('selected', light_blue)])

        tvstyle.configure("Trstyle.Treeview.Heading", foreground='black', font=(yekan, 15), )
        self.search_tv = ttk.Treeview(self.search_page, style="Trstyle.Treeview")
        self.search_tv.place(x=140, y=90)
        self.search_tv["columns"]=('guest_id','phone_number','nationality','gender','id', 'lastname', 'name', 'row')

        self.tv_scroll = ttk.Scrollbar(self.search_page, orient ="vertical", command=self.search_tv.yview)
        self.tv_scroll.place(x=141, y=91, height=229)
        self.search_tv.configure(yscrollcommand=self.tv_scroll.set)

        self.search_tv.heading('guest_id', text='شماره پذیرش')
        self.search_tv.heading('phone_number', text='شماره تماس')
        self.search_tv.heading('nationality', text='ملیت')
        self.search_tv.heading('gender', text='جنسیت')
        self.search_tv.heading('id', text='کد ملی')
        self.search_tv.heading('lastname', text= 'نام خانوادگی')
        self.search_tv.heading('name', text= 'نام')
        self.search_tv.heading('row', text='ردیف')

        self.search_tv.column('guest_id', width=150, anchor="c",minwidth= 60)
        self.search_tv.column('phone_number', width=150, anchor="c",minwidth= 60)
        self.search_tv.column('nationality', width=80, anchor="c", minwidth= 60)
        self.search_tv.column('gender', width=80, anchor="c", minwidth= 70)
        self.search_tv.column('id', width=150, anchor="c", minwidth= 75)
        self.search_tv.column('lastname', width=150, anchor="c", minwidth= 120)
        self.search_tv.column('name', width=150, anchor="c", minwidth= 60)
        self.search_tv.column('row', width=60, anchor="c", minwidth= 60)

        # changing row color by the tag given to the inserted items in the tree view
        self.search_tv.tag_configure('oddrow', background='#c9d3e6')
        self.search_tv.tag_configure('evenrow', background= '#e5eaf2')

        self.search_l = Label(self.search_page, text= ':یکی از گذینه های زیر را برای جستجو انتخاب کنید', font=(yekan,16), bg=white)
        self.search_l.place(relx= 0.40, rely=0.5)

        self.search_c = ttk.Combobox(self.search_page, values= ['نام', 'نام خانوادگی', 'کد ملی', 'جنسیت', 'ملیت', 'شماره تماس'], font= (yekan, 12), justify='center', width= 22)
        self.search_c.place(relx= 0.55, rely=0.65)

        self.search_e = ttk.Entry(self.search_page, font= (yekan, 12), justify="center", width= 25)
        self.search_e.place(relx= 0.35, rely=0.65)

        self.search_b = Button(self.search_page, text= 'جستجو', font= (yekan, 15), bg=dark_yellow, fg=black, highlightthickness=2, border=0,highlightbackground=light_yellow, highlightcolor=light_yellow, activebackground=light_yellow, activeforeground=black, width= 10, cursor='hand2', command= self.check_data)
        self.search_b.place(relx= 0.55, rely=0.80)

        self.delete_b = Button(self.search_page, text= 'حذف', font= (yekan, 15), bg=dark_yellow, fg=black, highlightthickness=2, border=0,highlightbackground=light_yellow, highlightcolor=light_yellow, activebackground=light_yellow, activeforeground=black, width= 10, cursor='hand2', command= self.client_deleter)
        self.delete_b.place(relx= 0.35, rely=0.80)
        
    def check_data(self):
        correctness = True
        if not(self.search_c.get()) or not(self.search_e.get()) :
            correctness = False
            self.error = Label(self.search_page, text=" لطفا همهء موارد فوق را پر کنید",fg="red",bg=white,font=(yekan,10))
            self.error.place(relx=0.45, rely=0.9)
            self.error.after(3000,self.error.destroy)
        if not(self.search_c.get()) :
            self.error = Label(self.search_page, text='*',fg="red",bg=white,font=(yekan,20))
            self.error.place(relx= 0.53, rely=0.64)
            self.error.after(3000,self.error.destroy)
        elif not (self.search_c.get())  == 'نام' and not (self.search_c.get())  == 'نام خانوادگی' and not (self.search_c.get())  == 'کد ملی' and not (self.search_c.get())  == 'جنسیت' and not (self.search_c.get())  == 'ملیت' and not (self.search_c.get())  == 'شماره تماس':
            correctness = False
            self.error = Label(self.search_page, text='فقط گذینه های مشخص شده',fg="red",bg=white,font=(yekan,12))
            self.error.place(relx= 0.55, rely=0.70)
            self.error.after(3000,self.error.destroy)
        if not(self.search_e.get()) :
            self.error = Label(self.search_page, text='*',fg="red",bg=white,font=(yekan,20))
            self.error.place(relx= 0.33, rely=0.64)
            self.error.after(3000,self.error.destroy)

        if correctness :
            pass

    def client_deleter (self):
        message = messagebox.askquestion("تایید","پاااکش کنم؟؟؟")

class PaymentPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        top_menu(self, controller)

        guests_side_page = Frame(self, bg= dark_gray)
        guests_side_page.pack(side= 'right', fill= Y)

        reception_button = Button(guests_side_page, text= 'دریافت مبلغ', font=(yekan, 12, 'bold'), bg=dark_gray, fg=black, highlightthickness=2, border=0, highlightbackground=dark_gray, highlightcolor=light_gray, activebackground=light_gray, activeforeground=black, width=10, cursor= 'hand2', command=lambda: controller.show_frame('PaymentPage'))
        reception_button.pack(side= 'top', pady= 15)

        checkout_button = Button(guests_side_page, text= 'تسویه حساب', font=(yekan,12, 'bold'),bg=dark_gray, fg=black, highlightthickness=2, border=0, highlightbackground=dark_gray, highlightcolor=light_gray, activebackground=light_gray, activeforeground=black, width=10, cursor= 'hand2', command=lambda: controller.show_frame("PaymentPage"))
        checkout_button.pack(side= 'top', pady= 15)

        payment_page = Frame(self, bg= 'white')
        payment_page.pack(side= 'right', fill= 'both', expand= True)

        reception_l = Label(payment_page, text= 'مبالغ دریافتی', font=(yekan, 30, 'bold'), bg= 'white')
        reception_l.pack(side= 'top')


if __name__ == "__main__":
    app = HotelApp()
    app.mainloop()