from os import system as bersih
from termcolor import colored as warna
from termcolor import cprint as cetak
from time import sleep as delay

gelombang = [0, 1, 2, 3, 4, 3, 2, 1]

def bendera(j):
    for baris in range(4):
        y = (j + baris) % len(gelombang)
        x = gelombang[y]
        print("   ", end="")
        cetak("|", "grey", "on_grey", end="")
        cetak(" " * x + " " * 25, "red", "on_red")

    for baris in range(4):
        y = (j + baris + 4) % len(gelombang)
        x = gelombang[y]
        print("   ", end="")
        cetak("|", "grey", "on_grey", end="")
        cetak(" " * x + " " * 25, "white", "on_white")

def tiang():
    for i in range(6):
        print("   ", end="")
        cetak("|", "grey", "on_grey")

def orang(jumlah=10):
    kepala = " o  "
    badan  = "/|\\ "
    kaki   = "/ \\ "
    print("\n" + "     " + kepala * jumlah)
    print("     " + badan * jumlah)
    print("     " + kaki * jumlah)

j = 0
while True:
    bersih("cls")
    bendera(j)
    tiang()
    orang(6)
    j += 1
    delay(0.1)