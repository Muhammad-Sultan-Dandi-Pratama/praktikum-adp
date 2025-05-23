while True:
    titik = []
    n = input("Berapa titik yang kamu mau ?  ")
    if n>'0':
        print(f"Baik {n} titik ya, tentukan nilai x dan y pada setiap titik tersebut : ")
        n=int(n)
        for i in range(n):
            print(f"\ntitik ke-{i+1}")
            x = float(input("nilai x: "))
            y = float(input("nilai y: "))
            titik.append([x, y])
        print("\nDaftar seluruh titik :")
        for i in range(n):
            print(f"titik ke-{i+1} = ({str(titik[i][0])}, {str(titik[i][1])})")
        print()
        for i in range(n):
            for j in range(i+1, n):
                titik_x = titik[i][0] - titik[j][0]
                titik_y = titik[i][1] - titik[j][1]
                jarak = (titik_x**2 + titik_y**2) ** 0.5
                print(f"Jarak titik {str(i+1)} ke titik {str(j+1)} = {str(jarak)}")
        break
    elif n<='0':
        print("masukan angka lebih dari 0")
