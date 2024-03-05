from tkinter import Frame, Label, Entry, Button, BOTH, END, Tk, W
from celsius import Celsius

class FrmCelcius:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES) 
        Label(mainFrame, text='Celcius:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Fahrenheit:").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Reamur:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Kelvin:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        
        self.txtCelcius = Entry(mainFrame) 
        self.txtCelcius.grid(row=0, column=1, padx=5, pady=5)  

        self.txtFahrenheit = Entry(mainFrame) 
        self.txtFahrenheit.grid(row=2, column=1, padx=5, pady=5) 

        self.txtReamur = Entry(mainFrame) 
        self.txtReamur.grid(row=3, column=1, padx=5, pady=5) 

        self.txtKelvin = Entry(mainFrame) 
        self.txtKelvin.grid(row=4, column=1, padx=5, pady=5) 

        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=1, column=1, padx=5, pady=5)

        # Result Labels
        self.lblFahrenheit = Label(mainFrame, text="")
        self.lblFahrenheit.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        self.lblReamur = Label(mainFrame, text="")
        self.lblReamur.grid(row=3, column=2, padx=5, pady=5, sticky=W)

        self.lblKelvin = Label(mainFrame, text="")
        self.lblKelvin.grid(row=4, column=2, padx=5, pady=5, sticky=W)
        
    def onHitung(self):
        C = Celsius(float(self.txtCelcius.get()))

        # Suhu dalam Fahrenheit
        F = C.get_fahrenheit()
        self.txtFahrenheit.delete(0, END)
        self.txtFahrenheit.insert(END, str(F))
        self.lblFahrenheit.config(text=f"Fahrenheit: {F} °F")

        # Suhu dalam Reamur
        R = C.get_reamur()
        self.txtReamur.delete(0, END)
        self.txtReamur.insert(END, str(R))
        self.lblReamur.config(text=f"Reamur: {R} °Re")

        # Suhu dalam Kelvin
        K = C.get_kelvin()
        self.txtKelvin.delete(0, END)
        self.txtKelvin.insert(END, str(K))
        self.lblKelvin.config(text=f"Kelvin: {K} K")
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmCelcius(root, "Program Konversi Suhu Celcius")
    root.mainloop()
