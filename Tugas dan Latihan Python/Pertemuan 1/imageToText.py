import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract

class ImageToTextConverter:
    def _init_(self, root):
        self.root = root
        self.root.title("Image to Text Converter")

        self.create_widgets()

    def create_widgets(self):
        # Frame untuk konten utama
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(pady=20)

        # Label untuk menampilkan gambar
        self.image_label = tk.Label(self.main_frame)
        self.image_label.grid(row=0, column=0, padx=20)

        # Button untuk memilih gambar
        self.browse_button = tk.Button(self.main_frame, text="Browse Image", command=self.load_image)
        self.browse_button.grid(row=1, column=0, pady=10)

        # Button untuk konversi teks
        self.convert_button = tk.Button(self.main_frame, text="Convert to Text", command=self.convert_to_text)
        self.convert_button.grid(row=2, column=0, pady=10)

        # Text untuk menampilkan hasil konversi
        self.result_text = tk.Text(self.main_frame, height=10, width=50)
        self.result_text.grid(row=3, column=0, pady=10)

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", ".png;.jpg;.jpeg;.gif;*.bmp")])

        if file_path:
            image = Image.open(file_path)
            self.display_image(image)

    def display_image(self, image):
        # Konversi gambar ke format yang dapat ditampilkan oleh Tkinter
        image = ImageTk.PhotoImage(image)

        # Menampilkan gambar pada label
        self.image_label.config(image=image)
        self.image_label.image = image

    def convert_to_text(self):
        # Mengambil gambar dari label
        image = Image.open(self.image_label.image)

        # Menggunakan pytesseract untuk melakukan OCR
        text = pytesseract.image_to_string(image)

        # Menampilkan hasil konversi pada Text widget
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, text)

if __name__ == "_main_":
    root = tk.Tk()
    app = ImageToTextConverter(root)
    root.mainloop()