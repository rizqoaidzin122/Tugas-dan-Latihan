# Rekursi Faktorial

n = int(input("Masukkan nilai yang ingin difaktorialkan: "))

def Faktorial (n):
    if n == 1:
        return (n)
    else:
        return (n*Faktorial(n-1))
    
print("%d! = %d" % (n, Faktorial(n)))
