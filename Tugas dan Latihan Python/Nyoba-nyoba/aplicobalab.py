import tkinter as tk

def hitung_hasil():
    hasil = 0
    # Lakukan perhitungan berdasarkan nilai yang dimasukkan
    # Misalnya, di sini kita hanya menambahkan nilai-nilai dari semua entri
    for entry in entries:
        nilai = float(entry.get())
        hasil += nilai
    # Tampilkan hasil di label_hasil
    label_hasil.config(text=f"Hasil: {hasil}")

# Membuat instance Tkinter
root = tk.Tk()
root.title("Aplikasi Pemeriksaan Lab")

# Membuat label dan entri untuk setiap tes yang ingin dilakukan
tes_lab = ["Tes1", "Tes2", "Tes3"] # Ganti dengan nama tes yang sesuai
entries = []
for i, tes in enumerate(tes_lab):
    label = tk.Label(root, text=tes)
    label.grid(row=i, column=0, padx=10, pady=5)  # Menggunakan grid manager untuk penempatan label
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)  # Menggunakan grid manager untuk penempatan entri
    entries.append(entry)

# Tombol untuk menghitung hasil
tombol_hitung = tk.Button(root, text="Hitung", command=hitung_hasil)
tombol_hitung.grid(row=len(tes_lab), column=0, columnspan=2, pady=10)  # Menggunakan grid manager untuk tombol

# Label untuk menampilkan hasil
label_hasil = tk.Label(root, text="")
label_hasil.grid(row=len(tes_lab)+1, column=0, columnspan=2)  # Menggunakan grid manager untuk hasil

# Menjalankan aplikasi
root.mainloop()
