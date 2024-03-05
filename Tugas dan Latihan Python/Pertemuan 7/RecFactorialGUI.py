import tkinter as tk
from tkinter import Entry, Label, Button

def Faktorial(n):
    if n == 1:
        return (n)
    else:
        return (n*Faktorial(n-1))

def hitung_Faktorial():
    try:
        nilai_n = int(entry_n.get())
        hasil = Faktorial(nilai_n)
        label_hasil.config(text=f"Faktorialnya adalah  {hasil}")
    except ValueError:
        label_hasil.config(text="Masukkan nilai yang valid")

# Membuat GUI dengan Tkinter
app = tk.Tk()
app.title("Program Penghitung Faktorial")

# Label dan Entry untuk memasukkan Faktorial
label_n = Label(app, text="Masukkan Angka:")
label_n.grid(row=0, column=0, padx=10, pady=10)
entry_n = Entry(app)
entry_n.grid(row=0, column=1, padx=10, pady=10)

# Button untuk menghitung Faktorial
button_hitung = Button(app, text="Hitung Faktorial", command=hitung_Faktorial)
button_hitung.grid(row=1, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil
label_hasil = Label(app, text="")
label_hasil.grid(row=2, column=0, columnspan=2, pady=10)

# Menjalankan program Tkinter
app.mainloop()