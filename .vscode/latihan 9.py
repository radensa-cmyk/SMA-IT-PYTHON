s = "Belajar Python itu Menyenangkan"

# a. Karakter pertama
print("Karakter pertama:", s[0])  # Output: B

# b. Karakter terakhir dengan indexing negatif
print("Karakter terakhir:", s[-1])  # Output: n

# c. Karakter spasi pertama (di indeks ke-7)
print("Spasi pertama:", s[7])  # Output: (spasi)

#2 Master Slicing

s = "Belajar Python itu Menyenangkan"

# a. "Python" (indeks 8 s/d 13)
print("Substring 'Python':", s[8:14])

# b. "Menyenangkan" (mulai dari indeks 19)
print("Substring 'Menyenangkan':", s[19:])

# c. "Belajar" (awal sampai indeks 6)
print("Substring 'Belajar':", s[:7])

#3

kata = input("Masukkan sebuah kata: ")

dibalik = kata[::-1]
print("Kata setelah dibalik:", dibalik)

if kata.lower() == dibalik.lower():
    print("Ini adalah palindrom!")
else:
    print("Bukan palindrom.")

#4

kalimat = "BPrOaGikRtoAdMiItMuINtuGhpPyYcThHoOnN"

kode_rahasia = kalimat[::3]
print("Kode Rahasia:", kode_rahasia)

#5

nama_salah = "dUDI sANTOSO"

# Ambil huruf pertama 'd', ubah jadi 'B'
huruf_depan = "B"
# Ambil "udi" dari indeks 1 sampai 3, ubah ke huruf kecil
bagian1 = nama_salah[1:4].lower()
# Ambil "S" dari indeks 5 dan sisanya "antoso" lalu betulkan
bagian2 = nama_salah[5].upper() + nama_salah[6:].lower()

# Gabungkan hasilnya
nama_benar = huruf_depan + bagian1 + " " + bagian2
print("Nama benar:", nama_benar)

