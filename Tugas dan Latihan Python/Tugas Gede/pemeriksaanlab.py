from db import DBConnection as mydb

class pemeriksaanlab:

    def __init__(self):
        self.__id = None
        self.__nomor_urut = None
        self.__nama_pasien = None
        self.__tanggal = None
        self.__jk = None
        self.__jenis_pemeriksaan = None
        self.__tarif = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def id(self):
        return self.__id

    @property
    def nomor_urut(self):
        return self.__nomor_urut

    @nomor_urut.setter
    def nomor_urut(self, value):
        self.__nomor_urut = value

    @property
    def nama_pasien(self):
        return self.__nama_pasien

    @nama_pasien.setter
    def nama_pasien(self, value):
        self.__nama_pasien = value

    @property
    def tanggal(self):
        return self.__tanggal

    @tanggal.setter
    def tanggal(self, value):
        self.__tanggal = value

    @property
    def jk(self):
        return self.__jk

    @jk.setter
    def jk(self, value):
        self.__jk = value

    @property
    def jenis_pemeriksaan(self):
        return self.__jenis_pemeriksaan

    @jenis_pemeriksaan.setter
    def jenis_pemeriksaan(self, value):
        self.__jenis_pemeriksaan = value

    @property
    def tarif(self):
        return self.__tarif

    @tarif.setter
    def tarif(self, value):
        self.__tarif = value


    def simpan(self):
        self.conn = mydb()
        val = (self.__nomor_urut, self.__nama_pasien, self.__tanggal, self.__jk, self.__jenis_pemeriksaan, self.__tarif)
        sql = "INSERT INTO pemeriksaanlab (nomor_urut, nama_pasien, tanggal, jk, jenis_pemeriksaan, tarif) VALUES (%s, %s, %s, %s, %s, %s)"
        self.affected = self.conn.insert(sql, val)
        self.conn.disconnect()
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__nomor_urut, self.__nama_pasien, self.__tanggal, self.__jk, self.__jenis_pemeriksaan, self.__tarif, id)
        sql = "UPDATE pemeriksaanlab SET nomor_urut = %s, nama_pasien = %s, tanggal = %s, jk = %s, jenis_pemeriksaan = %s, tarif = %s, WHERE id = %s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect()
        return self.affected

    def updateBynomor_urut(self, nomor_urut):
        self.conn = mydb()
        val = (self.__nama_pasien, self.__tanggal, self.__jk, self.__jenis_pemeriksaan, self.__tarif, nomor_urut)
        sql = "UPDATE pemeriksaanlab SET nama_pasien = %s, tanggal = %s, jk = %s, jenis_pemeriksaan = %s, tarif = %s WHERE nomor_urut = %s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect()
        return self.affected

    def delete(self, id):
        self.conn = mydb()
        sql = "DELETE FROM pemeriksaanlab WHERE id = %s"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect()
        return self.affected

    def deleteBynomor_urut(self, nomor_urut):
        self.conn = mydb()
        sql = "DELETE FROM pemeriksaanlab WHERE nomor_urut = '{}'".format(nomor_urut)
        self.affected = self.conn.delete(sql)
        self.conn.disconnect()
        return self.affected

    def getById(self, id):
        self.conn = mydb()
        sql = "SELECT * FROM pemeriksaanlab WHERE id = %s"
        self.result = self.conn.findOne(sql)
        self.__nomor_urut = self.result[1]
        self.__nama_pasien = self.result[2]
        self.__tanggal = self.result[3]
        self.__jk = self.result[4]
        self.__jenis_pemeriksaan = self.result[5]
        self.__tarif = self.result[6]
        self.conn.disconnect()
        return self.result

    def getBynomor_urut(self, nomor_urut):
        a = str(nomor_urut)
        b = a.strip()
        self.conn = mydb()
        sql = "SELECT * FROM pemeriksaanlab WHERE nomor_urut = %s"
        self.result = self.conn.findOne(sql, (b,))
        if self.result is not None:
            self.__nomor_urut = self.result[1]
            self.__nama_pasien = self.result[2]
            self.__tanggal = self.result[3]
            self.__jk = self.result[4]
            self.__jenis_pemeriksaan = self.result[5]
            self.__tarif = self.result[6]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nomor_urut = ''
            self.__nama_pasien = ''
            self.__tanggal = ''
            self.__jk = ''
            self.__jenis_pemeriksaan = ''
            self.__tarif = ''
            self.affected = 0
        self.conn.disconnect()
        return self.result
    
    def getAllData(self):
        self.conn = mydb()
        sql = "SELECT * FROM pemeriksaanlab"
        self.result = self.conn.findAll(sql)
        return self.result

A = pemeriksaanlab()
nomor_urut = '4444'
A.deleteBynomor_urut(nomor_urut)
B = A.getAllData()
print(B)
