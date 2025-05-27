def input_data():
    banyak = int(input("Masukkan jumlah praktikan: "))
    data = []

    for i in range(banyak):
        print("\nPraktikan ke-", i + 1)
        nama = input("Nama: ")
        nim = input("NIM: ")
        pretest = float(input("Nilai pretest: "))
        posttest = float(input("Nilai posttest: "))
        tugas = float(input("Nilai tugas/makalah: "))
        bonus = float(input("Nilai bonus: "))

        nilai_akhir = 0.25 * pretest + 0.25 * posttest + 0.5 * tugas + bonus
        praktikan = [nama, nim, pretest, posttest, tugas, bonus, nilai_akhir, 0]
        data.append(praktikan)

    return data

def ratarata_akhir(data):
    total = 0
    for i in range(len(data)):
        total = total + data[i][6]
    rata2 = total / len(data)
    return rata2

def peringkat(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j][6] < data[j + 1][6]:
                sementara = data[j]
                data[j] = data[j + 1]
                data[j + 1] = sementara
    for i in range(n):
        data[i][7] = i + 1

def tabel(data, rata2):
    print()
    print("Nama           NIM         NilaiAkhir     Peringkat")
    print("----------------------------------------------------")
    
    for i in range(len(data)):
        nama = data[i][0]
        nim = data[i][1]
        nilai_akhir = str(data[i][6])
        peringkat = str(data[i][7])

        spasi_nama = " " * (15 - len(nama))
        spasi_nim = " " * (12 - len(nim))
        spasi_nilai = " " * (15 - len(nilai_akhir))

        print(nama + spasi_nama + nim + spasi_nim + nilai_akhir + spasi_nilai + peringkat)
    
    print("----------------------------------------------------")
    print("Rata-rata nilai akhir: " + str(rata2))

# Program utama
data_praktikan = input_data()
rata2_nilai_akhir = ratarata_akhir(data_praktikan)
peringkat(data_praktikan)
tabel(data_praktikan, rata2_nilai_akhir)
