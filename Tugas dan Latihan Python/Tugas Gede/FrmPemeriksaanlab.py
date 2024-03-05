import tkinter as tk
from tkinter import Frame, Label, Entry, Button, ttk, END, messagebox
from tkcalendar import Calendar, DateEntry
from pemeriksaanlab import pemeriksaanlab  # Assuming Pemeriksaanlab is the class name


class FormPemeriksaanlab:   
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("550x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=tk.BOTH, expand=tk.YES)
        
        Label(mainFrame, text='Nomor Urut:').grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtnomor_urut = Entry(mainFrame) 
        self.txtnomor_urut.grid(row=0, column=1, padx=5, pady=5)

        Label(mainFrame, text='Nama Pasien:').grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtnama_pasien = Entry(mainFrame) 
        self.txtnama_pasien.grid(row=1, column=1, padx=5, pady=5)

        Label(mainFrame, text='Jenis Kelamin:').grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtJenis_Kelamin = ttk.Combobox(mainFrame, width=17)
        self.txtJenis_Kelamin['values'] = ('P', 'L')
        self.txtJenis_Kelamin.grid(row=2, column=1, padx=5, pady=5)

        Label(mainFrame, text='Tanggal:').grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtTanggal = DateEntry(mainFrame, width=16, background="magenta3", foreground="white", bd=2, date_pattern='y-mm-dd') 
        self.txtTanggal.grid(row=3, column=1, padx=5, pady=5)

        Label(mainFrame, text='Jenis Pemeriksaan:').grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtJenis_Pemeriksaan = ttk.Combobox(mainFrame, width=17)
        self.txtJenis_Pemeriksaan['values'] = ('Tes Darah', 'Tes Kolesterol', 'Tes Urine', 'Tes Hematologi Lengkap')
        self.txtJenis_Pemeriksaan.grid(row=4, column=1, padx=5, pady=5)

        Label(mainFrame, text='Tarif:').grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtTarif = Entry(mainFrame) 
        self.txtTarif.grid(row=5, column=1, padx=5, pady=5)
                
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        columns = ('ID', 'Nomor Urut', 'Nama Pasien', 'Jenis Kelamin', 'Tanggal', 'Jenis Pemeriksaan', 'Tarif')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.column('ID', width=30)
        self.tree.heading('Nomor Urut', text='Nomor Urut')
        self.tree.column('Nomor Urut', width=100)
        self.tree.heading('Nama Pasien', text='Nama Pasien')
        self.tree.column('Nama Pasien', width=100)
        self.tree.heading('Tanggal', text='Tanggal')
        self.tree.column('Tanggal', width=100)
        self.tree.heading('Jenis Kelamin', text='Jenis Kelamin')
        self.tree.column('Jenis Kelamin', width=100)
        self.tree.heading('Jenis Pemeriksaan', text='Jenis Pemeriksaan')
        self.tree.column('Jenis Pemeriksaan', width=100)
        self.tree.heading('Tarif', text='Tarif')
        self.tree.column('Tarif', width=100)
        self.tree.place(x=0, y=250)
        self.onReload()

    def onClear(self, event=None):
        self.txtnama_pasien.delete(0,END)
        self.txtnama_pasien.insert(END,"")                
        self.txtJenis_Kelamin.set("")
        self.txtJenis_Pemeriksaan.set("")
        self.txtTarif.delete(0,END)
        self.txtTarif.insert(END,"")                  
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False

    def onReload(self, event=None):
        plab = pemeriksaanlab()
        result = plab.getAllData()
        self.tree.delete(*self.tree.get_children())
        for row_data in result:
            self.tree.insert('', END, values=row_data)

    def onCari(self, event=None):
        nomor_urut = self.txtnomor_urut.get()
        plab = pemeriksaanlab()
        res = plab.getBynomor_urut(nomor_urut)
        rec = plab.affected
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
        return res
            
    def TampilkanData(self, event=None):
        nomor_urut = self.txtnomor_urut.get()
        plab = pemeriksaanlab()
        res = plab.getBynomor_urut(nomor_urut)
        self.txtnama_pasien.delete(0,END)
        self.txtnama_pasien.insert(END,res['nama_pasien'])     
        self.txtJenis_Kelamin.set(res['jk'])
        self.txtTanggal.delete(0,END)
        self.txtTanggal.insert(END,res['tanggal'])              
        self.txtJenis_Pemeriksaan.set(res['jenis_pemeriksaan'])
        self.txtTarif.delete(0,END)
        self.txtTarif.insert(END,res['tarif'])
        self.btnSimpan.config(text="Update")
        jk = res['jk']
        if jk == "P":
            self.P.select()
        else:
            self.L.select()

    def onSimpan(self, event=None):
        nomor_urut = self.txtnomor_urut.get()
        nama_pasien = self.txtnama_pasien.get()
        Jenis_Kelamin = self.txtJenis_Kelamin.get()
        Tanggal = self.txtTanggal.get_date()
        Jenis_Pemeriksaan = self.txtJenis_Pemeriksaan.get()
        Tarif = self.txtTarif.get()    

        plab = pemeriksaanlab()
        plab.nomor_urut = nomor_urut
        plab.nama_pasien = nama_pasien
        plab.jk = Jenis_Kelamin
        plab.tanggal = Tanggal
        plab.jenis_pemeriksaan = Jenis_Pemeriksaan
        plab.tarif = Tarif
        if self.ditemukan:
            res = plab.updateBynomor_urut()
            ket = 'Diperbarui'
        else:
            res = plab.simpan()
            ket = 'Disimpan'
            
        if res > 0:
            messagebox.showinfo("showinfo", f"Data Berhasil {ket}")
        else:
            messagebox.showwarning("showwarning", f"Data Gagal {ket}")
        self.onClear()
        return res

    def onDelete(self, event=None):
        nomor_urut = self.txtnomor_urut.get()
        plab = pemeriksaanlab()
        plab.nomor_urut = nomor_urut
        if self.ditemukan:
            res = plab.deleteBy()
            rec = plab.affected
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
    aplikasi = FormPemeriksaanlab(root, "Aplikasi Data Pemeriksaanlab")
    root.mainloop()
