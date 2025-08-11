# Langit biru membentang luas
# Mentari pagi bersinar terang
# Burung-burung pun bernyanyi

# Latihan 1: Tampilkan semua huruf kapital
nama_file = input("Masukkan nama file (contoh: puisi.txt): ")

try:
    with open(nama_file, 'r') as file:
        for baris in file:
            print(baris.strip().upper())
except FileNotFoundError:
    print("File tidak ditemukan!")

# Latihan 2: Rata-rata spam confidence
nama_file = input("Masukkan nama file (contoh: mbox-short.txt): ")

try:
    with open(nama_file, 'r') as file:
        total = 0
        jumlah = 0
        for baris in file:
            if baris.startswith("X-DSPAM-Confidence:"):
                angka = float(baris.strip().split(":")[1])
                total += angka
                jumlah += 1
        if jumlah > 0:
            rata_rata = total / jumlah
            print(f"Rata-rata spam confidence: {rata_rata}")
        else:
            print("Tidak ada data spam confidence ditemukan.")
except FileNotFoundError:
    print("File tidak ditemukan!")


# Latihan 3: Easter Egg file
nama_file = input("Masukkan nama file: ")

if nama_file.lower() == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
    try:
        with open(nama_file, 'r') as file:
            for baris in file:
                print(baris.strip().upper())
    except FileNotFoundError:
        print("File tidak ditemukan!")
