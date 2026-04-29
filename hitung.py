

def tambah(a, b):
    return a + b

print("5 + 3 =", tambah(5, 3))
def kali(a, b):
    return a * b

print("4 × 6 =", kali(4, 6))

def bagi(a, b):
    if b == 0:
        return "Error: Tidak bisa dibagi dengan nol"
    return a / b

print("9 : 2 =", bagi(9, 2))

def pecah(a, b): 
    return a + 2 * b

print("9 + 2*2 =", pecah(9, 2))

def kurang(a, b):
    return a - b

print("10 - 3 =", kurang(10, 3))

def kalkulator(a, b, operasi):
    if operasi == "tambah":
        return a + b
    elif operasi == "kali":
        return a * b
    elif operasi == "kurang":
        return a - b
    elif operasi == "bagi":
        if b == 0:
            return "Error: Tidak bisa dibagi dengan nol"
        return a / b
    elif operasi == "pecah":
        return a + 2 * b
    else:
        return "Operasi tidak dikenal"

print("Kalkulator: 8 + 2 =", kalkulator(8, 2, "tambah"))
print("Kalkulator: 8 * 2 =", kalkulator(8, 2, "kali"))
print("Kalkulator: 8 - 2 =", kalkulator(8, 2, "kurang"))
print("Kalkulator: 8 / 2 =", kalkulator(8, 2, "bagi"))
print("Kalkulator: 8 pecah 2 =", kalkulator(8, 2, "pecah"))
print("Kalkulator: 8 / 0 =", kalkulator(8, 0, "bagi"))
# Project Kalkulator Sederhana - Yohanes 2026
def kuadrat(x):
    return x * x

print("Kuadrat dari 5 =", kuadrat(5))
