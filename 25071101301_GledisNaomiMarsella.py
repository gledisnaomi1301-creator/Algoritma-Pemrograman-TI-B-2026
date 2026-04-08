# === BAGIAN A ===

DAFTAR_ANGKA = [23, 67, 4, 89, 15, 42, 73, 31, 58, 9]
angka_rahasia = 10
maks_percobaan = 8
nomor_ronde = 0


def tebak_angka(angka_rahasia, maks_percobaan):
    data = []

while True:
    angka_tebakan = int(input("Masukkan angka tebakan :"))

    if sisa_percobaan == 0:
        break

    if not angka_tebakan:
        print("input harus angka!")
        continue

    if angka_tebakan == angka_rahasia:
        print("benar")
        brhasil = True
        break

    elif angka_tebakan < angka_rahasia:
        print("angka lebih kecil!")
        sisa_percobaan = maks_percobaan -1
        continue

    else:
        print("angka lebih besar!")
        sisa_percobaan = maks_percobaan -1
        continue


def hitung_skor(berhasil, sisa_percobaan):
    for i in range(sisa_percobaan):
        if i == 0:
            return berhasil
        return
            

def main_satu_ronde(nama, nomor_ronde):
    angka_rahasia = DAFTAR_ANGKA[nomor_ronde]
    tebak_angka(maks_percobaan, angka_rahasia)
    skor = hitung_skor(berhasil,sisa_percobaan)
    return riwayat [nama,skor]
    return angka_rahasia
    return nomor_ronde 

#program utama
print("==Game Tebak Angka==")












    

