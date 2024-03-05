class Fahrenheit:
    def __init__(self, suhu):
        self.suhu = suhu

    def get_fahrenheit(self):
        return self.suhu

    def get_celcius(self):
        val = (5/9) * (float(self.suhu) - 32)
        return val

    def get_reamur(self):
        val = (4/9) * (float(self.suhu) - 32)
        return val

    def get_kelvin(self):
        val = (5/9) * (float(self.suhu) - 32) + 273
        return val

# Entry
suhu = input("Masukkan suhu dalam Fahrenheit: ")
F = Fahrenheit(float(suhu))
val = F.get_fahrenheit()

# Rumus
C = F.get_celcius()
R = F.get_reamur()
K = F.get_kelvin()

# Output
print(suhu + " Fahrenheit sama dengan:")
print(str(C) + " Celcius")
print(str(R) + " Reamur")
print(str(K) + " Kelvin")
