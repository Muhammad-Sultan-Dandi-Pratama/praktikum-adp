print("Kita akan menghitung probabilitas suatu variabel acak Poisson P(N(t) = n)")
print("untuk setiap n = 0, 1, 2, 3,..., M dengan parameter λt.")
print("Pertama tama...\n")
 
t = float(input("Masukkan Nilai λt : "))
m = int(input("Masukkan Batas n (n>=0) : "))
e = 2.71828

faktor = 1
p = e**-t

print(f"\nProbabilitas Variabel acak Poisson P(N(t) = n) dengan batas n = 0 hinnga {m} dan parameter λt {t} adalah...\n")

for n in range(0, m+1):
    print(f"P(N(t) = {n}) = {p:.5}\n")
    faktor = faktor * (n+1)
    p = p * (t / (n+1))
   
    