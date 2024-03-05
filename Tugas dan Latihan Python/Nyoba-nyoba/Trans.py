from googletrans import Translator

def translate_text(text, source_lang, target_lang):
    translator = Translator()
    translation = translator.translate(text, src=source_lang, dest=target_lang)
    return translation.text

def main():
    print("Selamat datang di Aplikasi Penerjemah Sederhana!")
    
    source_lang = input("Masukkan kode bahasa sumber (contoh: en): ")
    target_lang = input("Masukkan kode bahasa tujuan (contoh: id): ")
    
    while True:
        text_to_translate = input("Masukkan teks yang ingin diterjemahkan (atau ketik 'exit' untuk keluar): ")
        
        if text_to_translate.lower() == 'exit':
            print("Terima kasih! Sampai jumpa!")
            break
        
        translated_text = translate_text(text_to_translate, source_lang, target_lang)
        print(f"Hasil terjemahan: {translated_text}\n")

if __name__ == "__main__":
    main()