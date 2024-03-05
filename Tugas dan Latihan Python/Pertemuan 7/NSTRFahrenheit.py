print("konversi Suhu Fahrenheit")

#Entry
suhu = input("Masukkan suhu dalam Fahrenheit: ")

#rumus
R = 4/9*(float(suhu)-32)
C = 5/9*(float(suhu)-32)
K = 5/9*(float(suhu)-32) + 273.15

#output
print(suhu + " Fahrenheit sama dengan = ")
print(str(R)+" Reamur")
print(str(C)+" Celcius")
print(str(K)+" Kelvin")