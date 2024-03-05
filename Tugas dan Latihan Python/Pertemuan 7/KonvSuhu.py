from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W

class FrmCelcius:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='Celsius:').grid(row=0, column=0,sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Fahrenheit:").grid(row=2, column=0,sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Reamur:").grid(row=3, column=0,sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Kelvin:").grid(row=4, column=0,sticky=W, padx=5, pady=5)

        self.txtCelsius = Entry(mainFrame)
        self.txtCelsius.grid(row=0, column=1, padx=5, pady=5)

        self.txtFahrenheit = Entry(mainFrame)
        self.txtFahrenheit.grid(row=2, column=1, padx=5, pady=5)

        self.txtReamur = Entry(mainFrame)
        self.txtReamur.grid(row=3, column=1, padx=5, pady=5)

        self.txtKelvin = Entry(mainFrame)
        self.txtKelvin.grid(row=4, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung',command=self.onHitung)
        self.btnHitung.grid(row=1, column=1, padx=5, pady=5)

    def onHitung(self):
        try:
            # Input temperature in Celsius
            temperature_celsius = float(self.txtCelsius.get())

            # Convert to other scales
            temperature_fahrenheit = (temperature_celsius * 9/5) + 32
            temperature_reamur = temperature_celsius * 4/5
            temperature_kelvin = temperature_celsius + 273.15

            # Display results
            self.txtFahrenheit.delete(0, END)
            self.txtFahrenheit.insert(END, str(temperature_fahrenheit))

            self.txtReamur.delete(0, END)
            self.txtReamur.insert(END, str(temperature_reamur))

            self.txtKelvin.delete(0, END)
            self.txtKelvin.insert(END, str(temperature_kelvin))

        except ValueError:
            # Handle invalid input
            print("Error. Invalid Number")

    def onKeluar(self, event=None):
        # Close the application
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = FrmCelcius(root, "Program Konversi Suhu Celcius")
    root.mainloop()
