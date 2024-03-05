import tkinter as tk
from tkinter import ttk, messagebox
from Perawat import Perawat

class FormPerawat:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = ttk.Frame(self.parent, borderwidth=10)  # Use 'borderwidth' instead of 'bd'
        mainFrame.pack(fill=tk.BOTH, expand=tk.YES)
        
        # Label
        ttk.Label(mainFrame, text='NIP:').grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtNIP = ttk.Entry(mainFrame) 
        self.txtNIP.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNIP.bind("<Return>", self.onCari)

        ttk.Label(mainFrame, text='Nama:').grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtNama = ttk.Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5) 

        ttk.Label(mainFrame, text='JK:').grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtJK = ttk.Entry(mainFrame) 
        self.txtJK.grid(row=2, column=1, padx=5, pady=5) 

        # Button
        self.btnSimpan = ttk.Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = ttk.Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = ttk.Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # define columns
        columns = ('id', 'NIP', 'Nama', 'JK')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('NIP', text='NIP')
        self.tree.column('NIP', width="60")
        self.tree.heading('Nama', text='Nama')
        self.tree.column('Nama', width="200")
        self.tree.heading('JK', text='JK')
        self.tree.column('JK', width="30")
        # set tree position
        self.tree.place(x=0, y=200)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtNIP.delete(0, tk.END)
        self.txtNIP.insert(tk.END, "")
        self.txtNama.delete(0, tk.END)
        self.txtNama.insert(tk.END, "")       
        self.txtJK.delete(0, tk.END)
        self.txtJK.insert(tk.END, "")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data Perawat
        mk = Perawat()
        result = mk.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        subjects = []
        for row_data in result:
            subjects.append(row_data)

        for subject in subjects:
            self.tree.insert('', tk.END, values=subject)
    
    def onCari(self, event=None):
        NIP = self.txtNIP.get()
        mk = Perawat()
        res = mk.getByNIP(NIP)
        rec = mk.affected
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtNama.focus()
        return res
        
    def TampilkanData(self, event=None):
        NIP = self.txtNIP.get()
        mk = Perawat()
        res = mk.getByNIP(NIP)
        self.txtNama.delete(0, tk.END)
        self.txtNama.insert(tk.END, mk.Nama)
        self.txtJK.delete(0, tk.END)
        self.txtJK.insert(tk.END, mk.JK)   
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        NIP = self.txtNIP.get()
        Nama = self.txtNama.get()
        JK = self.txtJK.get()
        
        mk = Perawat()
        mk.NIP = NIP
        mk.Nama = Nama
        mk.JK = JK
        if self.ditemukan:
            res = mk.updateByNIP(NIP)
            ket = 'Diperbarui'
        else:
            res = mk.simpan()
            ket = 'Disimpan'
            
        rec = mk.affected
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        NIP = self.txtNIP.get()
        mk = Perawat()
        mk.NIP = NIP
        if self.ditemukan:
            res = mk.deleteByNIP(NIP)
            rec = mk.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormPerawat(root, "Aplikasi Data Perawat")
    root.mainloop()
