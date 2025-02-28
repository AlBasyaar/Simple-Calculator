def tambah(a, b):
    hasil = a + b
    print(f"Hasil dari {a} + {b} = {hasil}")

def kurang(a, b):
    hasil = a - b  # Perbaikan dari '+' ke '-'
    print(f"Hasil dari {a} - {b} = {hasil}")

def kali(a, b):
    hasil = a * b  # Perbaikan dari '+' ke '*'
    print(f"Hasil dari {a} x {b} = {hasil}")

def bagi(a, b):
    if b != 0:
        hasil = a / b  # Perbaikan dari '+' ke '/'
        print(f"Hasil dari {a} : {b} = {hasil}")
    else:
        print("Error: Tidak bisa membagi dengan nol!")

# Loop utama program
while True:
    try:
        a = int(input("Nilai A : "))
        b = int(input("Nilai B : "))
    except ValueError:
        print("Masukkan angka yang valid!")
        continue

    jenis = input("[1]Tambah\n[2]Kurang\n[3]Kali\n[4]Bagi\n[5]Keluar\nPilih : ")

    if jenis == "1":
        tambah(a, b)
    elif jenis == "2":
        kurang(a, b)
    elif jenis == "3":
        kali(a, b)
    elif jenis == "4":
        bagi(a, b)
    elif jenis == "5":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")
