# Nama File: Perawat.py
from db import DBConnection as mydb

class Perawat:

    def __init__(self):
        self.__id = None
        self.__NIP = None
        self.__Nama = None
        self.__JK = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def id(self):
        return self.__id

    @property
    def NIP(self):
        return self.__NIP

    @NIP.setter
    def NIP(self, value):
        self.__NIP = value

    @property
    def Nama(self):
        return self.__Nama

    @Nama.setter
    def Nama(self, value):
        self.__Nama = value

    @property
    def JK(self):
        return self.__JK

    @JK.setter
    def JK(self, value):
        self.__JK = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__NIP, self.__Nama, self.__JK)
        sql = "INSERT INTO Perawat (NIP, Nama, JK) VALUES (%s, %s, %s)"
        self.affected = self.conn.insert(sql, val)
        self.conn.disconnect()
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__NIP, self.__Nama, self.__JK, id)
        sql = "UPDATE Perawat SET NIP = %s, Nama = %s, JK = %s WHERE id = %s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect()
        return self.affected

    def updateByNIP(self, NIP):
        self.conn = mydb()
        val = (self.__Nama, self.__JK, NIP)
        sql = "UPDATE Perawat SET Nama = %s, JK = %s WHERE NIP = %s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect()
        return self.affected

    def delete(self, id):
        self.conn = mydb()
        sql = "DELETE FROM Perawat WHERE id = %s"
        self.affected = self.conn.delete(sql, (id,))
        self.conn.disconnect()
        return self.affected

    def deleteByNIP(self, NIP):
        self.conn = mydb()
        sql = "DELETE FROM Perawat WHERE NIP = %s"
        self.affected = self.conn.delete(sql, (NIP,))
        self.conn.disconnect()
        return self.affected

    def getById(self, id):
        self.conn = mydb()
        sql = "SELECT * FROM Perawat WHERE id = %s"
        self.result = self.conn.findOne(sql, (id,))
        self.__NIP = self.result[1]
        self.__Nama = self.result[2]
        self.__JK = self.result[3]
        self.conn.disconnect()
        return self.result

    def getByNIP(self, NIP):
        a = str(NIP)
        b = a.strip()
        self.conn = mydb()
        sql = "SELECT * FROM Perawat WHERE NIP = %s"
        self.result = self.conn.findOne(sql, (b,))
        if self.result is not None:
            self.__NIP = self.result[1]
            self.__Nama = self.result[2]
            self.__JK = self.result[3]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__NIP = ''
            self.__Nama = ''
            self.__JK = ''
            self.affected = 0
        self.conn.disconnect()
        return self.result
    
    def getAllData(self):
        self.conn = mydb()
        sql = "SELECT * FROM Perawat"
        self.result = self.conn.findAll(sql)
        return self.result

A = Perawat()
NIP = '4444'
A.deleteByNIP(NIP)
B = A.getAllData()
print(B)
