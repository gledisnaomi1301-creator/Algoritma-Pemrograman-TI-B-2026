#kodisi basis
def jumlah_digit(n):
    if n == 0:          
        return 0
    return n % 10 + jumlah_digit(n // 10)

# pemanggilan
angka = 1234
hasil = jumlah_digit(angka)

print(hasil)