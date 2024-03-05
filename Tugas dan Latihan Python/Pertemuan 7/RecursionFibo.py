#rumus fib
n=int(input("Masukkan suku ke-: "))

def Bilangan_fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return (Bilangan_fibonacci(n-1) + Bilangan_fibonacci(n-2))

if __name__ == "__main__":
    print("Deret Bilangan Fibonaccinya adalah : ")

for i in range(n):
    print(Bilangan_fibonacci(i), end=' ')