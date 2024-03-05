import tkinter as tk
from tkinter import messagebox
from Dashboard import Dashboard
from Users import Users

class FormLogin:
    def __init__(self, update_main_window):
        self.update_main_window = update_main_window
        self.root = tk.Tk()
        self.root.title("Login")
        self.root.geometry("250x150")

        self.label_username = tk.Label(self.root, text='Username:')
        self.label_username.place(x=20, y=20)
        self.label_password = tk.Label(self.root, text='Password:')
        self.label_password.place(x=20, y=50)

        self.txtusername = tk.Entry(self.root)
        self.txtusername.place(x=100, y=20, width=120)
        self.txtpassword = tk.Entry(self.root, show="*")
        self.txtpassword.place(x=100, y=50, width=120)

        btnSubmit = tk.Button(self.root, text='Submit', command=self.onSubmit)
        btnSubmit.place(x=20, y=90, width=100, height=30)
        btnCancel = tk.Button(self.root, text='Cancel', command=self.root.quit)
        btnCancel.place(x=130, y=90, width=100, height=30)

    def onSubmit(self):
        username = self.txtusername.get()
        password = self.txtpassword.get()

        obj = Users()
        if obj.login(username, password):
            self.update_main_window(True)
            self.root.withdraw()  # Menyembunyikan form login
            self.showDashboard()
            messagebox.showinfo("Login Berhasil", "Login berhasil!")
        else:
            messagebox.showwarning("Login Gagal", "Username atau password salah!")
            print("Percobaan gagal:", obj.validation)

    def showDashboard(self):
        root = tk.Tk()
        dashboard = Dashboard(root)
        root.mainloop()

    def run(self):
         self.root.mainloop()

if __name__ == '__main__':
    def update_main_window(result):
        print(result)

    form_login = FormLogin(update_main_window)
    form_login.run()
