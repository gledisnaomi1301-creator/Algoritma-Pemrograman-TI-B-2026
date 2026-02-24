class PO_Attacca:
    
    def __init__(self, nama_pembeli):
        self.nama = nama_pembeli
        self.harga_album = 350000
        self.harga_pc = 50000
        
    def detail_album(self):
        return "Album: Attacca - SEVENTEEN"
        
    def hitung_total(self):
        try:
            jumlah_album = int(input("\nJumlah album yang dipesan: "))
            jumlah_pc = int(input("Jumlah photocard tambahan: "))
            
            if jumlah_album <= 0:
                raise ValueError("Jumlah album harus lebih dari 0")
            
            total_album = jumlah_album * self.harga_album
            total_pc = jumlah_pc * self.harga_pc
            total_bayar = total_album + total_pc
            
        except ValueError as e:
            print("\nError:", e)
        else:
            print("\n=== Detail Pesanan ===")
            print("Nama Pembeli :", self.nama)
            print(self.detail_album())
            print("Jumlah Album :", jumlah_album)
            print("Photocard    :", jumlah_pc)
            print("Total Bayar  : Rp", total_bayar)
            print("\nSetiap album mendapatkan 1 photocard random member!")
        finally:
            print("\nProgram selesai.")


pembeli1 = PO_Attacca("Carat_Gledis")

print("=== Program PO Album Attacca SEVENTEEN ===")
print("Nama Pembeli:", pembeli1.nama)
print(pembeli1.detail_album())

pembeli1.hitung_total()