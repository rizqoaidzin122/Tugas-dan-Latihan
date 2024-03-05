print("konversi Suhu Kelvin")

#Entry
suhu = input("Masukkan suhu dalam Kelvin")

#rumus
F = (9/5*float(suhu))+32
C = (5/5*float(suhu))-273
R = (5/9*float(suhu))-273

#output
print(suhu + " Reamur sama dengan")
print(str(F)+" Fahrenheit")
print(str(C)+" Celcius")
print(str(R)+" Reamur")