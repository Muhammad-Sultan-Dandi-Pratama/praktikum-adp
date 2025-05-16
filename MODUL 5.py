data_mahasiswa = []

while True:
    print("\nMenu Utama:")
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampilkan Data")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        nama = input("Masukkan nama mahasiswa : ")
        nilai = int(input("Masukkan nilai mahasiswa : "))
        nomor = input("Masukkan nomor mahasiswa : ")
        data_mahasiswa.append([nomor, nama, nilai])
        print("Data berhasil ditambahkan.")

    elif pilihan == "2":
        hapus = input("Masukkan nomor mahasiswa yang ingin dihapus: ")
        index = -1
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == hapus:
                index = i
                break
        if index != -1:
            del data_mahasiswa[index]
            print("Data berhasil dihapus.")
        else:
            print("Data tidak ditemukan.")

    elif pilihan == "3":
        if len(data_mahasiswa) == 0:
            print("Belum ada data mahasiswa.")
        else:
            urutan = []
            for i in range(len(data_mahasiswa)):
                urutan.append(data_mahasiswa[i])
            for i in range(len(urutan)):
                for j in range(i + 1, len(urutan)):
                    if urutan[i][2] < urutan[j][2]:
                        sementara = urutan[i]
                        urutan[i] = urutan[j]
                        urutan[j] = sementara
            for mahasiswa in urutan:
                print("Nomor:", mahasiswa[0], "| Nama:", mahasiswa[1], "| Nilai:", mahasiswa[2])

    elif pilihan == "4":
        print("Terima kasih! Program sudah selesai :).")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1-4.")
