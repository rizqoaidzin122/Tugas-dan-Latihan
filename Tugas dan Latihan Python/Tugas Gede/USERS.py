from db import DBConnection 

class Users:
    def __init__(self):
        self.db = DBConnection()
        self.validation = 0  # Menyimpan jumlah percobaan gagal

    def login(self, username, password):
        val = (username, password)
        sql = "SELECT * FROM `login` WHERE `username` = %s AND `password` = %s"
        result = self.db.findOne(sql, val)
        if result:
            # Reset nilai percobaan gagal jika login berhasil
            self.validation = 0
            return True
        else:
            # Tambahkan jumlah percobaan gagal
            self.validation += 3
            return False

# Contoh penggunaan:
login_system = Users()

# Contoh login
username = "misnen"
password = "12345"
if login_system.login(username, password):
    print("Login berhasil!")
else:
    print("Username atau password salah!")
    print("Percobaan gagal:", login_system.validation)
