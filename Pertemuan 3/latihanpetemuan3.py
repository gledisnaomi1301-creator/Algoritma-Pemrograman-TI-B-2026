#INHERITANCE 

class Produk:
    def __init__(self, nama_produk, harga):
        self.nama_produk = nama_produk
        self.harga = harga

    def info_produk(self):
        return f"Nama Produk: {self.nama_produk}\nHarga: Rp{self.harga}"


class ProdukElektronik(Produk):
    def __init__(self, nama_produk, harga, garansi):
        super().__init__(nama_produk, harga)
        self.garansi = garansi  # dalam tahun

    def info_produk(self):
        return (f"Nama Produk: {self.nama_produk}\n"
                f"Harga: Rp{self.harga}\n"
                f"Garansi: {self.garansi} tahun")


class ProdukMakanan(Produk):
    def __init__(self, nama_produk, harga, tanggal_kadaluarsa):
        super().__init__(nama_produk, harga)
        self.tanggal_kadaluarsa = tanggal_kadaluarsa

    def info_produk(self):
        return (f"Nama Produk: {self.nama_produk}\n"
                f"Harga: Rp{self.harga}\n"
                f"Tanggal Kadaluarsa: {self.tanggal_kadaluarsa}")


produk1 = ProdukElektronik("Laptop", 30000000, 2)
produk2 = ProdukMakanan("Biskuit", 15000, "12-12-2026")

print("Produk Elektronik")
print(produk1.info_produk())

print("\n Produk Makanan")
print(produk2.info_produk())




#POLYMORPHISM

class Notifikasi:
    def kirim(self):
        return "Mengirim notifikasi umum"


class Email(Notifikasi):
    def kirim(self):
        return "Mengirim notifikasi melalui Email"


class SMS(Notifikasi):
    def kirim(self):
        return "Mengirim notifikasi melalui SMS"


notifikasi_umum = Notifikasi()
notifikasi_email = Email()
notifikasi_sms = SMS()

print(notifikasi_umum.kirim())
print(notifikasi_email.kirim())
print(notifikasi_sms.kirim())



#ENCAPSULATION

class Mahasiswa:
    def __init__(self):
        self.__nilai = 0   # atribut private

    def set_nilai(self, nilai):
        if 0 <= nilai <= 100:
            self.__nilai = nilai
        else:
            return "Nilai tidak valid"

    def get_nilai(self):
        return self.__nilai


mhs = Mahasiswa()

print(mhs.set_nilai(85))     # valid
print("Nilai:", mhs.get_nilai())

print(mhs.set_nilai(120))    # tidak valid
print("Nilai:", mhs.get_nilai())






  




   


   
  