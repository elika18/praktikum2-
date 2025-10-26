# Program Mengurutkan Data

# Input jumlah data (minimal 3)
n = int(input("Masukkan jumlah data (minimal 3): "))

if n < 3:
    print("Jumlah data minimal 3!")
else:
    data = []
    for i in range(n):
        bil = int(input(f"Bilangan ke-{i+1}: "))
        data.append(bil)

    # Mengurutkan data dari kecil ke besar
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i] > data[j]:
                # Tukar posisi
                data[i], data[j] = data[j], data[i]

    # Tampilkan hasil
    print("Urutan bilangan:", end=" ")
    for bil in data:
        print(bil, end=" ")