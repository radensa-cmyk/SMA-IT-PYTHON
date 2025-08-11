# Mulai dari angka 10
angka = 10

# Loop selama angka lebih besar dari 0
while angka > 0:
    print(angka)
    angka -= 1  # Kurangi angka setiap iterasi

# Setelah selesai menghitung mundur
print("Blastoff!")


#2

import random

# Simpan sebuah angka rahasia di dalam variabel
angka_rahasia = random.randint(1, 10) # Angka rahasia antara 1 dan 10

print("Selamat datang di Game Tebak Angka!")
print("Saya sudah menyimpan sebuah angka antara 1 dan 10. Coba tebak!")

while True:
    try:
        # Minta pengguna untuk menebak angka
        tebakan = int(input("Masukkan tebakan Anda: "))

        # Gunakan if untuk mengecek tebakan
        if tebakan == angka_rahasia:
            print("selamat, anda benar!")
            break  # Keluar dari loop jika tebakan benar
        else:
            print("maaf,anda gagal")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

print("Terima kasih sudah bermain!")


#3

total = 0
jumlah_angka = 0

print("Selamat datang di program Input Angka Cerdas!")
print("Masukkan angka satu per satu. Ketik 'done' untuk mengakhiri.")

while True:
    input_pengguna = input("Masukkan angka: ")

    if input_pengguna.lower() == 'done':
        break  # Keluar dari loop jika pengguna mengetik 'done'

    try:
        angka = float(input_pengguna)  # Gunakan float untuk mengakomodasi angka desimal
        total += angka
        jumlah_angka += 1
    except ValueError:
        print("Input tidak valid. Harap masukkan angka atau 'done'.")
        continue  # Lanjut ke iterasi berikutnya tanpa memproses input yang salah

print("\n--- Ringkasan ---")
print(f"Total              : {total}")
print(f"Jumlah angka       : {jumlah_angka}")

if jumlah_angka > 0:
    rata_rata = total / jumlah_angka
    print(f"Rata-rata          : {rata_rata}")
else:
    print("Tidak ada angka yang dimasukkan untuk dihitung rata-ratanya.")

print("Terima kasih telah menggunakan program ini!")