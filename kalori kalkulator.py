import time
import os
from termcolor import colored, cprint
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.prompt import Prompt, IntPrompt, FloatPrompt

console = Console()
# fungsi append kata kata berwarna
def add(text_obj, content="",  style=None, newline=False, blank_line=False):
    text_obj.append(content, style)
    if newline:
        text_obj.append("\n")
    if blank_line:
        text_obj.append("\n")

# Fungsi animasi loading
def loading(teks="Memproses"):
    for i in range(3):
        print(f"{teks}{'.' * (i+1)}", end='\r')
        time.sleep(0.5)
    print(" " * 20, end='\r')

# Fungsi saran kesehatan
def saran_kesehatan(jenis, hasil):
    if jenis == "BMI":
        if hasil < 16:
            text = Text()
            add(text,"KEKURUSAN PARAH","underline bold red", newline=True)
            add(text,"Saran","bold underline blue", newline=True)
            add(text,"Segera konsultasikan ke ")
            add(text,"dokter","yellow")
            add(text," atau ")
            add(text,"ahli gizi","yellow")
            add(text,". Risiko ")
            add(text,"malnutrisi serius","red")
            add(text," dan fungsi tubuh terganggu (lihat opsi 3 kalkulator ")
            add(text,"BMI", "bold cyan")
            add(text,").")
            return console.print(text, width=80)
        elif 16 <= hasil < 18.5:
            text = Text()
            add(text,"KEKURUSAN RINGAN-SEDANG","underline red", newline=True)
            add(text,"Saran","bold underline blue", newline=True)
            add(text,"tingkatkan ")
            add(text,"asupan nutrisi seimbang","green")
            add(text," dan  ")
            add(text,"tambahkan kalori","green")
            add(text," harian Anda untuk mencapai berat badan ")
            add(text,"ideal","bold green")
            add(text,".")
            return console.print(text, width=80)
        elif 18.5 <= hasil <= 25:
            text = Text()
            add(text,"IDEAL","underline bold green", newline=True)
            add(text,"Saran","bold underline blue", newline=True)
            add(text,"BAGUS!","green")
            add(text," Terus pertahankan ")
            add(text,"pola makan seimbang","green")
            add(text," dan ")
            add(text,"olahraga teratur","green")
            add(text," untuk menjaga kesehatan tubuh.")
            return console.print(text, width=80)
        elif 25 < hasil <= 30:
            text = Text()
            add(text,"KEGEMUKAN","underline bold yellow", newline=True)
            add(text,"Saran","bold underline blue", newline=True)
            add(text,"Perhatikan ")
            add(text,"pola makan","green")
            add(text," dan tingkatkan ")
            add(text,"aktivitas fisik","green")
            add(text," untuk menghindari kelebihan berat badan yang lebih serius.")
            return console.print(text, width=80)
        elif 30 < hasil <= 40:
            text = Text()
            add(text,"OBESITAS KELAS I & II","underline red", newline=True)
            add(text,"Saran","bold underline blue", newline=True)
            add(text,"Risiko kesehatan meningkat","red")
            add(text,". Disarakankan menurunkan berat badan secara bertahap dengan ")
            add(text,"pola makan seimbang","green")
            add(text," dan ")
            add(text,"olahraga teratur","green")
            add(text,".")
            return console.print(text, width=80)
        elif hasil > 40:
            text = Text()
            add(text,"OBESITAS KELAS III","underline bold red", newline=True)
            add(text,"Saran","bold underline blue", newline=True)
            add(text,"TERMASUK OBESITAS MORBID","red")
            add(text,". ")
            add(text,"Bahaya penyakit mengintai","red")
            add(text," (baca opsi 2 kalkulator ")
            add(text,"BMI", "bold cyan")
            add(text,"). Sangat disarankan untuk segera berkonsultasi dengan ")
            add(text,"dokter spesialis","yellow")
            add(text," untuk penanganan intensif.")
            return console.print(text, width=80)
    elif jenis == "Kalori":
        return "Pastikan kebutuhan kalori sesuai aktivitas harian Anda."
    elif jenis == "BMR":
        return "Gunakan BMR untuk mengatur pola makan yang tepat."
    elif jenis == "Body Fat":
        return "Persentase lemak tubuh penting untuk kesehatan jantung dan metabolisme."
    return "Jaga selalu gaya hidup sehat!"

# Fungsi menyimpan ke file .txt
def simpan_riwayat_kalori(data):
    with open("riwayat.txt", "a") as file:
        file.write(data + "\n")
def simpan_riwayat_bmi(jenis, hasil):
    with open("Riwayat_BMI.txt", "a") as file:
        file.write(f"{jenis}: {hasil:.2f}\n")
# 
# Fungsi-fungsi kalkulasi
#

##### KALKULATOR BMI ✅
def pengenalan_bmi():
    # Definisi BMI
    text = Text()
    add(text,"BMI", "bold cyan")
    add(text," adalah pengukuran ")
    add(text,"KELANGSINGAN", "green") 
    add(text," atau ")
    add(text,"KEGEMUKAN", "red")
    add(text," seseorang berdasarkan berat badan dan tinggi badannya. Ini secara luas digunakan sebagai indikator umum apakah seseorang memiliki berat badan yang sehat untuk tinggi badannya.", newline=True)
    add(text,"Rentang ")
    add(text,"BMI", "bold cyan")
    add(text," ini bervariasi berdasarkan faktor-faktor seperti wilayah dan usia, dan terkadang dibagi lagi menjadi subkategori seperti ")
    add(text,"SANGAT KEKURANGAN BERAT BADAN", "red")
    add(text," atau ")
    add(text,"SANGAT OBESITAS", "red", newline=True)
    add(text,blank_line=True)
    add(text,"Berikut adalah klasifikasi ")
    add(text,"BMI", "bold cyan")
    add(text," berdasarkan ")
    add(text,"World Health Organization (WHO)", "italic blue")
    add(text," untuk orang dewasa : ")
    console.print(text, width=80)
    print()
    # tabel klasifikasi BMI
    table = Table(title="Klasifikasi BMI")
    table.add_column("Klasifikasi")
    table.add_column("Kisaran BMI - kg/m²")
    data = [
        ["Kekurusan Parah", "< 16"],
        ["Kekurusan Sedang", "16 - 17"],
        ["Kekurusan Ringan", "17 - 18.5"],
        ["Normal", "18.5 - 25"],
        ["Kegemukan", "25 - 30"],
        ["Obesitas Kelas I", "30 - 35"],
        ["Obesitas Kelas II", "35 - 40"],
        ["Obesitas Kelas III", "> 40"]
    ]
    for row in data:
        table.add_row(*row)
    console.print(table)

def hitung_bmi():
    berat = float(input("Masukkan berat badan (kg): "))
    tinggi = float(input("Masukkan tinggi badan (cm): ")) / 100
    bmi = berat / (tinggi ** 2)
    loading("Menghitung BMI")
    print(f"\n✅ BMI Anda: {bmi:.2f}")
    print("💡",end=' ') 
    saran_kesehatan("BMI", bmi)
    simpan_riwayat_bmi("BMI", bmi)
    
def risiko_kelebihan_berat_badan():
    text = Text()
    
    # Judul
    add(text, "Risiko yang berhubungan dengan ", style="bold")
    add(text, "KELEBIHAN BERAT BADAN", style="bold red", newline=True)
    add(text, blank_line=True)
    # Paragraf pengantar
    add(text, "KELEBIHAN BERAT BADAN", style="bold red")
    add(text, " meningkatkan risiko sejumlah penyakit dan kondisi kesehatan serius. Berikut ini adalah daftar risiko tersebut, menurut ")
    add(text, "Centers for Disease Control and Prevention (CDC)", style="italic blue")
    add(text, ":", newline=True)
    add(text, blank_line=True)
    # Daftar poin risiko
    risiko_list = [
        "Tekanan darah tinggi",
        "Kadar kolesterol LDL yang lebih tinggi, kadar HDL lebih rendah, dan trigliserida tinggi",
        "Diabetes tipe II",
        "Penyakit jantung koroner",
        "Stroke",
        "Penyakit kandung empedu",
        "Osteoartritis (kerusakan sendi)",
        "Apnea tidur dan masalah pernapasan",
        "Kanker tertentu (endometrium, payudara, ginjal, hati, kantong empedu)",
        "Kualitas hidup rendah",
        "Penyakit mental seperti depresi dan kecemasan",
        "Nyeri tubuh dan gangguan fungsi fisik",
        "Secara umum, risiko kematian meningkat"
    ]

    for item in risiko_list:
        add(text, f"• {item}", style="red", newline=True)
    
    add(text, blank_line=True)

    # Penutup
    add(text, "Kelebihan berat badan bisa menimbulkan ")
    add(text, "dampak negatif", style="red")
    add(text, " dan bahkan ")
    add(text, "berakibat fatal", style="red")
    add(text, ".", newline=True)

    add(text, "Menjaga ")
    add(text, "BMI", style="bold cyan")
    add(text, " di bawah 25 dan berkonsultasi dengan ")
    add(text, "dokter", style="yellow")
    add(text, " membantu hidup lebih ")
    add(text, "sehat", style="green")
    add(text, ".", newline=True)
    
    console.print(text, width=80)

def risiko_kekurangan_berat_badan():
    text = Text()
    
    # Judul
    add(text, "Risiko yang berhubungan dengan ", style="bold")
    add(text, "KEKURANGAN BERAT BADAN", style="bold red", newline=True)
    add(text, blank_line=True)

    # Paragraf pengantar
    add(text,"KEKURANGAN BERAT BADAN", style="bold red")
    add(text, " memiliki risiko terkaitnya sendiri, yang tercantum di bawah ini:", newline=True)
    add(text, blank_line=True)

    # Daftar risiko
    risiko_list = [
        "Malnutrisi, kekurangan vitamin, anemia (penurunan kemampuan pembuluh darah)",
        "Osteoporosis, penyakit yang menyebabkan tulang menjadi lemah, sehingga meningkatkan risiko patah tulang",
        "Penurunan fungsi kekebalan tubuh",
        "Masalah pertumbuhan dan perkembangan, terutama pada anak-anak dan remaja",
        "Kemungkinan masalah reproduksi pada wanita karena ketidakseimbangan hormon yang dapat mengganggu siklus menstruasi",
        "Wanita dengan berat badan kurang juga memiliki risiko keguguran yang lebih tinggi pada trimester pertama.",
        "Potensi komplikasi akibat operasi",
        "Secara umum, risiko kematian meningkat dibandingkan dengan mereka yang memiliki BMI sehat"
    ]

    for item in risiko_list:
        add(text, f"• {item}", style="red", newline=True)
    add(text, blank_line=True)

    # Paragraf penutup
    add(text, "Dalam beberapa kasus, ")
    add(text, "kekurangan berat badan", style="bold red")
    add(text, " dapat menjadi tanda dari beberapa kondisi atau penyakit yang mendasarinya seperti ")
    add(text, "anoreksia nervosa", style="red")
    add(text, ", yang memiliki risiko tersendiri. Konsultasikan dengan ")
    add(text, "dokter", style="yellow")
    add(text, " jika Anda merasa Anda atau seseorang yang Anda kenal kekurangan berat badan, terutama jika alasan ")
    add(text, "kekurangan berat badan", style="bold red")
    add(text, " tersebut tidak tampak jelas.", newline=True)

    console.print(text, width=80)

def kalkulator_bmi():
    while True:
        print(f"""
==============================
🧮 KALKULATOR BMI
==============================
1. Pengenalan BMI
2. Resiko kelebihan Berat Badan
3. Resiko kekurangan Berat Badan
4. Hitung BMI
0. Keluar
""")
        pilihan = input("Pilih opsi (0-5): ")
        os.system("cls")
        if pilihan == '1':
            pengenalan_bmi()
        elif pilihan == '2':
            risiko_kelebihan_berat_badan()
        elif pilihan == '3':
            risiko_kekurangan_berat_badan()
        elif pilihan == '4':
            hitung_bmi()
        elif pilihan == '0':
            break
        else:
            print("❌ Pilihan tidak valid. Coba lagi.")
        input("\nTekan Enter untuk kembali ke menu Kalkulator BMI...")
        os.system("cls")


##### KALKULATOR KALORI
def input_data():
    console.rule("[bold cyan]🔢 Masukkan Data Anda")

    age = IntPrompt.ask("Umur (15 - 80 tahun)")
    gender = Prompt.ask("Jenis kelamin", choices=["male", "female"])
    height = FloatPrompt.ask("Tinggi badan (cm)", default=170)
    weight = FloatPrompt.ask("Berat badan (kg)", default=65)

    # Tabel aktivitas
    console.print("\n[bold cyan]Pilih tingkat aktivitas harian kamu:[/bold cyan]\n")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Kode", justify="center")
    table.add_column("Aktivitas")
    table.add_column("Keterangan")

    aktivitas = [
        ("1", "BMR", "Tidak aktif sama sekali"),
        ("2", "Sedentary", "Sedikit atau tidak latihan"),
        ("3", "Light", "Latihan 1–3x/minggu"),
        ("4", "Moderate", "Latihan 4–5x/minggu"),
        ("5", "Active", "Latihan intens 3-4x/minggu"),
        ("6", "Very Active", "Latihan intens 6–7x/minggu"),
        ("7", "Extra Active", "Pekerjaan fisik atau Latihan sangat intens setiap hari")
    ]

    for kode, nama, ket in aktivitas:
        table.add_row(kode, nama, ket)

    console.print(table)

    # Penjelasan tambahan
    console.print("\n[bold]Catatan:[/bold]")
    console.print("• [cyan]Exercise[/cyan]: 15–30 menit aktivitas dengan detak jantung meningkat.")
    console.print("• [cyan]Intense exercise[/cyan]: 45–120 menit aktivitas dengan detak jantung meningkat.")
    console.print("• [cyan]Very intense exercise[/cyan]: lebih dari 2 jam aktivitas dengan detak jantung meningkat.\n")

    activity_code = Prompt.ask("Masukkan kode aktivitas (1–7)", choices=[str(i) for i in range(1, 8)])
    return age, gender, height, weight, int(activity_code)

def hitung_bmr(age, gender, height, weight):
    if gender == "male":
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

def faktor_aktivitas(kode):
    return {
        1: 1.0,
        2: 1.2,
        3: 1.375,
        4: 1.465,
        5: 1.55,
        6: 1.725,
        7: 1.9
    }.get(kode, 1.2)

def tampilkan_hasil(bmr, tdee):
    console.rule("[bold green]📊 Hasil Perhitungan")
    table = Table(show_header=False)
    table.add_row("Basal Metabolic Rate (BMR)", f"[cyan]{round(bmr, 2)}[/cyan] kalori/hari")
    table.add_row("Total Daily Energy Expenditure (TDEE)", f"[green]{round(tdee, 2)}[/green] kalori/hari")
    console.print(table)

def hitung_kalori():
    age, gender, height, weight, activity_code = input_data()
    bmr = hitung_bmr(age, gender, height, weight)
    tdee = bmr * faktor_aktivitas(activity_code)
    tampilkan_hasil(bmr, tdee)
    simpan_riwayat_kalori(f"Kalkulator Kalori - BMR: {round(bmr, 2)} kalori, TDEE: {round(tdee, 2)} kalori")
    # Langsung tampilkan simulasi
    console.print("\n[bold cyan]🎯 Simulasi Tujuan[/bold cyan]")
    kalori_cutting = tdee * 0.8
    kalori_bulking = tdee * 1.15

    console.print(f"• [red]Cutting (Defisit 20%)[/red]: [bold]{round(kalori_cutting, 2)}[/bold] kcal/hari")
    console.print(f"• [yellow]Maintenance[/yellow]: [bold]{round(tdee, 2)}[/bold] kcal/hari")
    console.print(f"• [green]Bulking (Surplus 15%)[/green]: [bold]{round(kalori_bulking, 2)}[/bold] kcal/hari")

def kalkulator_kalori():
    while True:
        print(f"""
==============================
🧮 KALKULATOR KALORI
==============================
1. Hitung kalori harian
2. Hitung Kalori
0. Keluar
""")
        pilihan = input("Pilih opsi (0-5): ")
        os.system("cls")
        if pilihan == '1':
            hitung_kalori()
        elif pilihan == '2':
            hitung_kalori()
        elif pilihan == '0':
            break
        else:
            print("❌ Pilihan tidak valid. Coba lagi.")
        input("\nTekan Enter untuk kembali ke menu Kalkulator Kalori...")
        os.system("cls")

##### LIHAT RIWAYAT
def tampilkan_riwayat():
    print("\n📜 Riwayat Perhitungan:")
    if os.path.exists("riwayat_kalkulator.txt"):
        with open("riwayat_kalkulator.txt", "r") as file:
            print(file.read())
    else:
        print("Belum ada riwayat tersimpan.")

# Menu utama
def main():
    while True:
        print("""
==============================
🧮 KALKULATOR KESEHATAN
==============================
1. Kalkulator BMI
2. Kalkulator Kalori
3. Lihat Riwayat
0. Keluar
""")
        pilihan = input("Pilih kalkulator (0-5): ")
        os.system("cls")
        if pilihan == '1':
            kalkulator_bmi()
        elif pilihan == '2':
            kalkulator_kalori()
        elif pilihan == '3':
            tampilkan_riwayat()
            input("\nTekan Enter untuk kembali ke menu utama...")
        elif pilihan == '0':
            print("👋 Terima kasih telah menggunakan kalkulator kesehatan!")
            break
        else:
            print("❌ Pilihan tidak valid. Coba lagi.")
            input("\nTekan Enter untuk kembali ke menu utama...")
        os.system("cls")




if __name__ == "__main__":
    main()