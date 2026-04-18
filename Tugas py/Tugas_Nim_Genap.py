def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def perkalian_rekursif(m, n):
    if n == 0:
        return 0
    elif n == 1:
        return m
    else:
        return m + perkalian_rekursif(m, n - 1)

def main():
    while True:
        print("\nNim Genap")
        print("menu pilihan")
        print("1. Barisan Fibonacci")
        print("2. M Kali N")
        print("0. Keluar")
        
        pilihan = input("Pilih Menu : ")

        if pilihan == '1':
            jumlah = int(input("Masukkan Jumlah Suku : "))
            print(f"barisan fibonacci sebanyak {jumlah} suku :")
            hasil = []
            for i in range(1, jumlah + 1):
                hasil.append(str(fibonacci(i)))
            print(", ".join(hasil))

        elif pilihan == '2':
            m = int(input("Masukkan Suatu Bilangan Bulat : "))
            n = int(input("Masukkan Suatu Bilangan Pengali : "))
            hasil = perkalian_rekursif(m, n)
            print(f"{m} x {n} = {hasil}")

        elif pilihan == '0':
            print("Keluar dari program...")
            break
        
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()