import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from translate import translate

def translate_text():
    text_to_translate = entry.get()
    selected_language = destination_language.get()
    translator = Translator()
    translated_text = translator.translate(text_to_translate, dest=selected_language)
    translated_box.delete(1.0, tk.END)
    translated_box.insert(tk.END, translated_text.text)


# Membuat GUI
root = tk.Tk()
root.title("TRANSLATOR")
root.resizable(width=False, height=False)

# Mengatur warna background
root.configure(bg="#00FFFF")

# Menambahkan style untuk tombol
style = ttk.Style()
style.configure("TButton", foreground="white", background="#4CAF50")

label = tk.Label(root, text="Masukkan Teks:", bg="#EFEFEF", fg="black", font=("Times New Roman", 12))
label.pack(pady=(10, 5))

entry = tk.Entry(root, font=("Times New Roman", 12))
entry.pack(pady=(0, 5))

destination_language_label = tk.Label(root, text="Pilih Bahasa:", bg="#EFEFEF", fg="black", font=("Times New Roman", 12))
destination_language_label.pack(pady=(0, 5))

# Menambahkan pilihan
languages = ['English', 'Filipino', 'vietnam']
destination_language = ttk.Combobox(root, values=languages, state="readonly", font=("Times New Roman", 12))
destination_language.pack(pady=(0, 5))

translate_button = tk.Button(root, text="Translate", command=translate_text, font=("Algerian", 12), bg="#FAEBD7", fg="black")  # Ganti dengan warna font, latar belakang, dan warna tombol yang diinginkan
translate_button.pack(pady=(10, 5))

# Mengatur wrap pada kolom teks untuk mengikuti panjang teks
translated_box = tk.Text(root, height=10, width=40, wrap=tk.WORD, font=("Arial", 12))
translated_box.pack(pady=(0, 10))

root.geometry("300x400")
root.mainloop()

