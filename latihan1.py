# Program menampilkan tabel angka dengan nested for

# Banyak kolom
kolom = 10

# Baris akan terus bertambah sampai angka terakhir (pojok kanan bawah) = 18
# Karena baris dimulai dari 0, maka baris terakhir = 9 (0–9 → 10 baris)
baris = 10

for i in range(baris):
    for j in range(kolom):
        # Cetak angka dengan jarak rapi
        print(f"{i + j:2}", end="  ")
    print()  # ganti baris 