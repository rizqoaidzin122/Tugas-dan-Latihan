import tkinter as tk
from googletrans import Translator

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Translator")

        self.languages = ["en", "es", "fr", "id", "it"]  # Supported languages: English, Spanish, French, Indonesia, Italian

        self.source_language_label = tk.Label(root, text="Bahasa Asal:")
        self.source_language_label.grid(row=0, column=0, padx=10, pady=5)

        self.source_language_entry = tk.StringVar()
        self.source_language_dropdown = tk.OptionMenu(root, self.source_language_entry, *self.languages)
        self.source_language_dropdown.grid(row=0, column=1, padx=10, pady=5)

        self.target_language_label = tk.Label(root, text="Bahasa Target:")
        self.target_language_label.grid(row=1, column=0, padx=10, pady=5)

        self.target_language_entry = tk.StringVar()
        self.target_language_dropdown = tk.OptionMenu(root, self.target_language_entry, *self.languages)
        self.target_language_dropdown.grid(row=1, column=1, padx=10, pady=5)

        self.text_label = tk.Label(root, text="Enter Text:")
        self.text_label.grid(row=2, column=0, padx=10, pady=5)

        self.text_entry = tk.Entry(root, width=30)
        self.text_entry.grid(row=2, column=1, padx=10, pady=5)

        self.translate_button = tk.Button(root, text="Translate", command=self.translate_text)
        self.translate_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def translate_text(self):
        source_lang = self.source_language_entry.get()
        target_lang = self.target_language_entry.get()
        text_to_translate = self.text_entry.get()

        if source_lang and target_lang and text_to_translate:
            translator = Translator()
            translation = translator.translate(text_to_translate, src=source_lang, dest=target_lang)
            self.result_label.config(text=f"Translation: {translation.text}")
        else:
            self.result_label.config(text="Isi dengan Benar!.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
