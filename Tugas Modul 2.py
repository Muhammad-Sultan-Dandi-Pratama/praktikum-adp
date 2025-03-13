# INPUT HARGA PAKET
A = 30000
B = 50000
C = 50000
D = 75000
E = 100000
print("<====== SELAMAT DATANG DI RESTORAN RYUGU RENA ======> \n")
nama = input("Masukkan nama Anda : ")
telp = int(input("Masukkan Nomor telepon Anda : "))

print ("\n<====== PILIH PAKET MAKANAN ANDA ======>")

print("\nPaket A : Nasi goreng, Es teh. (Rp.30.000)")
print("\nPaket B : Ayam Bakar, Nasi putih, Es Teh. (Rp.50.000)")
print("\nPaket C : Ayam geprek, Nasi putih, Es Teh. (Rp.50.000) ")
print("\nPaket D : 2 Ayam geprek, Nasi putih, Es Teh. (Rp.75.000)")
print("\nPaket E : 1 Ekor ayam bakar JUMBO. (Rp.100.000)\n")
 
paket = input("Pilih paket mana? ")
jml = int(input("Mau berapa paket? "))
Alamat = input("Mau di antarin ke mana nih?  ")

# HARGA TOTAL
if paket == "A":
    harga = A * jml
elif paket == "B":
    harga = B * jml
elif paket == "C":
    harga = C * jml
elif paket == "D":
    harga = D * jml
elif paket == "E":
    harga = E * jml

# PAJAK
pajak = harga * 0.1

# BIAYA PENGIRIMAN
if harga < 150000:
    kirim = 25000
elif harga >= 150000:
    kirim = 0

# BIAYA AKHIR
akhir = harga + pajak + kirim

# STRUK PEMESANAN
print("\n<========== STRUK PEMESANAN ANDA =========>\n")
print(f"Nama : {nama}")
print(f"Nomor telepon : {telp}")
print(f"Alamat pengiriman di : {Alamat}")
print(f"\nDetail pemesanan : PAKET {paket}")
print(f"jumlah : {jml} paket")
print(f"Total harga : Rp.{harga:,}")
print(f"Pajak (10%) : Rp.{pajak:,}")
print(f"Biaya pengiriman : Rp.{kirim:,}")
print(f"\nTotal Akhir : Rp.{akhir:,}")
print(f"\n<============ TERIMA KASIH ============>")