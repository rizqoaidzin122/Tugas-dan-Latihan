# Menghitung Volume dan Luas Permukaan Balok

p = "Panjang"
l = "Lebar"
t = "Tinggi"

P = float(input('Masukkan Panjang: '))
L = float(input('MAsukkan Lebar: '))
T = float(input('Masukkan Tinggi: '))

V = P * L * T
LP = 2*(P*L + P*T + L*T)

print ("Volumenya adalah: ", V)
print ("Luas Permukannya adalah: ", LP)
