from tkinter import *
from tkinter import messagebox
import pickle

root = Tk()
root.title("Registration form")
root.geometry("500x600")


def regist_in():
    regist = Label(root, text="Зарегистрируйтесь для входа в систему")
    login_label = Label(root, text="Your login: ")
    login = Entry()
    password_label = Label(root, text="Your password: ")
    password = Entry()
    password_ag_label = Label(root, text="Enter  your password again: ")
    password_ag = Entry(show="*")
    btn_reg = Button(root, text="Register", command=lambda: save())
    regist.pack()
    login_label.pack()
    login.pack()
    password_label.pack()
    password.pack()
    password_ag_label.pack()
    password_ag.pack()
    btn_reg.pack()

    def save():
        if password.get() == password_ag.get():
            login_pass_save = {}
            login_pass_save[login.get()] = password.get()
            f = open("login.txt", "wb")
            pickle.dump(login_pass_save, f)
            f.close()
            log_in()

        else:
            messagebox.showerror("Error!", "Passwords does not match!")



def log_in():
    log__in = Label(root, text="Вход в систему")
    login_lb = Label(root, text="Enter your login: ")
    login = Entry()
    password_lb = Label(root, text="Enter your password: ")
    password = Entry(show="*")
    btn_in = Button(root, text="Enter!", command=lambda: log_pass())
    log__in.pack()
    login_lb.pack()
    login.pack()
    password_lb.pack()
    password.pack()
    btn_in.pack()

    def log_pass():
        f = open("login.txt", "rb")
        a = pickle.load(f)
        f.close()
        if login.get() in a:
            if password.get() == a[login.get()]:
                messagebox.showinfo("Ok", "Hi! You have new messages!")
            else:
                messagebox.showerror("Error!", "Wrong login or password!")
        else:
            messagebox.showerror("Error!", "Something wrong,please try again!")


regist_in()

root.mainloop()