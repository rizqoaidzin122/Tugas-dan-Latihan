import tkinter as tk
from tkinter import Entry, Label, Button

def Bilangan_fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return (Bilangan_fibonacci(n-1) + Bilangan_fibonacci(n-2))
    
    for i in range(n):
        print(Bilangan_fibonacci(i), end=' ')

def hitung_Fibo():
    try:
        nilai_n = int(entry_n.get())
        hasil = Bilangan_fibonacci(nilai_n)
        label_hasil.config(text=f"Deret Fibonaccinya adalah  {hasil}")
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
button_hitung = Button(app, text="Hitung Faktorial", command=hitung_Fibo)
button_hitung.grid(row=1, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil
label_hasil = Label(app, text="")
label_hasil.grid(row=2, column=0, columnspan=2, pady=10)

# Menjalankan program Tkinter
app.mainloop()