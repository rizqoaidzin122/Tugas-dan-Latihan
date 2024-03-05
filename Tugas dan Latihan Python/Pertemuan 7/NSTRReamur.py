print("konversi Suhu Reamur")

#Entry
suhu = input("Masukkan suhu dalam Reamur")

#rumus
F = (9/4*float(suhu))+32
C = (5/9*float(suhu))
K = (5/9*float(suhu))+273

#output
print(suhu + "Reamur sama dengan")
print(str(F)+" Fahrenheit")
print(str(C)+" Celcius")
print(str(K)+" Kelvin")