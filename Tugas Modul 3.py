print("Kita akan menghitung probabilitas suatu variabel acak Poisson P(N(t) = n)")
print("untuk setiap n = 0, 1, 2, 3,..., M dengan parameter λt.")
print("Pertama tama...\n")

t = float(input("Masukkan Nilai λt : "))
m = int(input("Masukkan Batas n (n>=0) : "))
e = 2.71828

for n in range(0, m+1):
    faktor = 1
    i = 1
    while i <= n:
        faktor *= i
        i += 1

P = (e**(-t) * (t**n)) / faktor
print(f"Probabilitas Variabel acak Poisson P(N(t) = n) dengan batas n {m} dan parameter λt {t} adalah... ")
print(f"P(N(t) = {m}) = {P}\n")