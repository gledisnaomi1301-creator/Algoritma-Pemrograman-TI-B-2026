# MLBB Ranking System

def input_pemain():
    """Menginput data pemain Mobile Legends"""
    data = []

    while True:
        nama = input("Masukkan nama pemain (ketik 'stop' untuk berhenti): ")
        
        if nama.lower() == "stop":
            break
        
        kill = int(input("Jumlah kill: "))
        death = int(input("Jumlah death: "))
        
        # panggil fungsi lain
        kda = hitung_kda(kill, death)
        rank = tentukan_rank(kda)
        
        # simpan ke list
        data.append([nama, kill, death, kda, rank])
    
    return data


def hitung_kda(kill, death):
    """Menghitung KDA pemain"""
    if death == 0:
        return kill  # hindari pembagian nol
    return kill / death


def tentukan_rank(kda):
    """Menentukan rank berdasarkan KDA"""
    if kda >= 5:
        return "Mythic"
    elif kda >= 3:
        return "Legend"
    elif kda >= 2:
        return "Epic"
    else:
        return "Grandmaster"


def tampilkan_pemain(data):
    """Menampilkan data pemain"""
    if len(data) == 0:
        print("Belum ada data pemain!")
    else:
        print("\n=== Data Pemain Mobile Legends ===")
        for pemain in data:
            print(f"Nama: {pemain[0]}, Kill: {pemain[1]}, Death: {pemain[2]}, KDA: {pemain[3]:.2f}, Rank: {pemain[4]}")


# ===== PROGRAM UTAMA =====

def main():
    """Fungsi utama"""
    daftar_pemain = input_pemain()
    tampilkan_pemain(daftar_pemain)


# jalankan program
main()