# Latihan 1: Mencetak kelipatan 7 dari 0 hingga 70
for i in range(0, 71, 7):
    print(i)


#2
#: Membalik string dengan for loop
kalimat = "Python"
kebalikan = ""

for huruf in kalimat:
    kebalikan = huruf + kebalikan  # tambahkan huruf di depan string baru

print("Kalimat asli:", kalimat)
print("Kebalikan  :", kebalikan)

#3

# Latihan 3: Mencari angka yang habis dibagi 3 dan 5
jumlah = 0  # Variabel akumulator untuk menghitung jumlah

for angka in range(1, 51):  # Iterasi dari 1 sampai 50
    if angka % 3 == 0 and angka % 5 == 0:
        print(angka)  # Tampilkan angka yang memenuhi syarat
        jumlah += 1   # Tambahkan ke hitungan

print("Jumlah angka yang habis dibagi 3 dan 5:", jumlah)


#4

# Latihan 4: Membuat pola segitiga siku-siku terbalik
for i in range(5, 0, -1):  # Mulai dari 5 turun ke 1
    for j in range(i):     # Cetak '*' sebanyak i kali
        print("*", end="")  # Cetak tanpa pindah baris
    print()  # Pindah baris setelah setiap baris bintang selesai

#5

# Meminta input dari pengguna
n = int(input("Masukkan bilangan bulat positif: "))

# Inisialisasi akumulator untuk hasil faktorial
hasil_faktorial = 1

# Menghitung faktorial dengan for loop
for i in range(1, n + 1):
    hasil_faktorial *= i  # Sama dengan hasil_faktorial = hasil_faktorial * i

# Menampilkan hasil
print(f"Faktorial dari {n} adalah {hasil_faktorial}")

