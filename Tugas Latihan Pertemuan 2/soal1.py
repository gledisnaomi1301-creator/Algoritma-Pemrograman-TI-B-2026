def rata_rata(nilai):
    if not nilai:
        return "Data kosong"
    return sum(nilai) / len(nilai)

# Panggil fungsi
data_nilai = [80, 75, 90, 60, 85]
hasil = rata_rata(data_nilai)

# Tampilkan hasil
print(hasil)