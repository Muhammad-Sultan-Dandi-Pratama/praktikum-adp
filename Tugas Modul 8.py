FILE_NAME = "data_keuangan.txt"

def file_ada(nama_file):
    file = open(nama_file, "a")

def load_data():
    data = []
    file_ada(FILE_NAME)
    file = open(FILE_NAME, "r")
    for line in file:
        parts = line.strip().split("|")
        if len(parts) == 4:
            tanggal = parts[0]
            keterangan = parts[1]
            jumlah = parts[2]
            tipe = parts[3]
            if jumlah.isdigit():
                data.append({
                    "tanggal": tanggal,
                    "keterangan": keterangan,
                    "jumlah": int(jumlah),
                    "tipe": tipe
                })
    file.close()
    return data


def save_data(data):
    file = open(FILE_NAME, "w")
    for item in data:
        line = item["tanggal"] + "|" + item["keterangan"] + "|" + str(item["jumlah"]) + "|" + item["tipe"] + "\n"
        file.write(line)
    file.close()

def tampilkan_data(data):
    if len(data) == 0:
        print("\nBelum ada data keuangan.")
    else:
        print("\n===== Daftar Data Keuangan =====")
        for i in range(len(data)):
            item = data[i]
            print(str(i + 1) + ". [" + item["tanggal"] + "] " + item["tipe"].upper() + " - " + item["keterangan"] + " : Rp" + str(item["jumlah"]))

def tambah_data(data):
    tanggal = input("Masukkan tanggal (YYYY-MM-DD): ")
    keterangan = input("Masukkan keterangan: ")
    jumlah = input("Masukkan jumlah uang: ")
    tipe = input("Tipe (pengeluaran/pemasukan): ").lower()

    if tipe != "pengeluaran" and tipe != "pemasukan":
        print("Tipe tidak valid.")
        return

    if not jumlah.isdigit():
        print("Jumlah harus berupa angka.")
        return

    data_baru = {
        "tanggal": tanggal,
        "keterangan": keterangan,
        "jumlah": int(jumlah),
        "tipe": tipe
    }

    data.append(data_baru)
    save_data(data)
    print("Data berhasil ditambahkan!")

def hapus_data(data):
    tampilkan_data(data)
    if len(data) == 0:
        return
    nomor = input("Masukkan nomor data yang ingin dihapus: ")
    if not nomor.isdigit():
        print("Input harus berupa angka.")
        return
    idx = int(nomor) - 1
    if idx < 0 or idx >= len(data):
        print("Nomor tidak valid.")
        return
    else:
        del data[idx]
        save_data(data)
        print("Data berhasil dihapus.")

def menu():
    data = load_data()
    while True:
        print("\n===== MENU KEUANGAN =====")
        print("1. Tambah data keuangan")
        print("2. Hapus data keuangan")
        print("3. Tampilkan semua data")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            tambah_data(data)
        elif pilihan == "2":
            hapus_data(data)
        elif pilihan == "3":
            tampilkan_data(data)
        elif pilihan == "4":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")
menu()