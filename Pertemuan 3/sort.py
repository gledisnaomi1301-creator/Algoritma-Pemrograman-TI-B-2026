def selection_sort(data):
    """Mengurutkan data berdasarkan nilai (descending)"""
    for i in range(len(data)):
        max_index = i
        for j in range(i+1, len(data)):
        
            if data[j][1] > data[max_index][1]:
                max_index = j
        
        
        data[i], data[max_index] = data[max_index], data[i]


def tampilkan_leaderboard(data):
    """Menampilkan hasil ranking"""
    for i in range(len(data)):
        print(f"{i+1}. {data[i][0]} - {data[i][1]}")


# ===== DATA AWAL =====
data = [
    ["Andi", 90],
    ["Budi", 85]
]

# ===== PROSES =====
selection_sort(data)

# ===== OUTPUT =====
tampilkan_leaderboard(data)