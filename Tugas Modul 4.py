m = int(input("Masukkan jumlah baris kursi: "))
n = int(input("Masukkan jumlah kolom kursi: "))

total_kursi = m * n
kursi_tersedia = ""
for i in range(1, total_kursi + 1):
    kursi_tersedia += str(i) + " "

print("\nSelamat datang di sistem reservasi tiket konser YOASOBI!")
print("\nHarga Tiket:")
print("VVIP: Rp1,000,000")
print("VIP: Rp800,000")
print("Reguler: Rp500,000")
print("Ekonomi: Rp300,000")

# Layout kursi
print("\nTampilan Layout Kursi:")
nomor_kursi = 1
for i in range(m):
    for j in range(n):
        print(nomor_kursi, end="  ")
        nomor_kursi += 1
    print()

jumlah_pemesanan = int(input("\nMasukkan jumlah tiket yang ingin dipesan: "))

for i in range(jumlah_pemesanan):
    print(f"\nPemesanan ke-{i+1}:")
    nama = input("Masukkan nama Anda: ")

    while True:
        no_kursi = input("Masukkan nomor kursi yang ingin dipesan: ")

        # cek kursi
        kursi_ada = False
        kursi_tersedia_baru = ""
        temp_kursi = ""

        for kurs in kursi_tersedia:
            if kurs != " ":
                temp_kursi += kurs
            else:
                if temp_kursi == no_kursi:
                    kursi_tersedia_baru += "0 "
                    kursi_ada = True
                else:
                    kursi_tersedia_baru += temp_kursi + " "
                temp_kursi = ""

        if kursi_ada:
            kursi_tersedia = kursi_tersedia_baru  
            break
        print("Kursi sudah dipesan atau tidak valid, silakan pilih kursi lain.")

    password = input("Buat password untuk akses konser: ")
    
    # Menentukan kategori
    no_kursi = int(no_kursi)
    baris_kursi = (no_kursi - 1) // n + 1
    if baris_kursi <= 2:
        kategori_kursi = "VVIP"
        harga = 1000000
    elif 3 <= baris_kursi <= 5:
        kategori_kursi = "VIP"
        harga = 800000
    elif 6 <= baris_kursi <= 15:
        kategori_kursi = "Reguler"
        harga = 500000
    else:
        kategori_kursi = "Ekonomi"
        harga = 300000

    
    print("\n<====== Struk Pemesanan Tiket ======>")
    print(f"Nama: {nama}\nNomor Kursi: {no_kursi}\nKategori: {kategori_kursi}")
    print(f"Harga: Rp{harga:,}\nPassword: {password}")
    print("-------------------------")

# Sisa kursi
sisa_vvip = 0
sisa_vip = 0
sisa_reguler = 0
sisa_ekonomi = 0

temp_kursi = ""
for kurs in kursi_tersedia:
    if kurs != " ":
        temp_kursi += kurs
    else:
        if temp_kursi != "0":
            kursi_num = int(temp_kursi)
            baris_kursi = (kursi_num - 1) // n + 1
            if baris_kursi <= 2:
                sisa_vvip += 1
            elif 3 <= baris_kursi <= 5:
                sisa_vip += 1
            elif 6 <= baris_kursi <= 15:
                sisa_reguler += 1
            else:
                sisa_ekonomi += 1
        temp_kursi = ""

print("\nSisa kursi per kategori:")
print(f"VVIP: {sisa_vvip}")
print(f"VIP: {sisa_vip}")
print(f"Reguler: {sisa_reguler}")
print(f"Ekonomi: {sisa_ekonomi}")

print("\nLayout Kursi Setelah Pemesanan:")
nomor_kursi = 1
temp_kursi = ""
for kurs in kursi_tersedia:
    if kurs != " ":
        temp_kursi += kurs
    else:
        print(temp_kursi, end="  ")
        temp_kursi = ""
        if nomor_kursi % n == 0:
            print()
        nomor_kursi += 1

print("\n<========== TERIMA KASIH ==========>")
