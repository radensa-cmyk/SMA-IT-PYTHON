# log_kegiatan.py
# Program ini berfungsi sebagai buku catatan (log) kegiatan.

# Membuka file log_kegiatan.txt dalam mode append
with open("log_kegiatan.txt", "a") as file:
    kegiatan = input("Masukkan kegiatan yang baru saja dilakukan: ")
    file.write(kegiatan + "\n")  # setiap entri di baris baru

print("Kegiatan berhasil dicatat di log_kegiatan.txt")



# salin_file.py
# Program ini menyalin isi sumber.txt ke salinan.txt

# Membuat file sumber.txt (jika belum ada)
with open("sumber.txt", "w") as sumber_file:
    sumber_file.write("Ini baris pertama.\n")
    sumber_file.write("Ini baris kedua.\n")
    sumber_file.write("Ini baris ketiga.\n")

# Membaca isi sumber.txt
with open("sumber.txt", "r") as sumber:
    isi = sumber.read()

# Menulis isi ke salinan.txt
with open("salinan.txt", "w") as salinan:
    salinan.write(isi)

print("Isi sumber.txt berhasil disalin ke salinan.txt")


# hapus_file.py
import os

# Meminta nama file
nama_file = input("Masukkan nama file yang ingin dihapus: ")

# Mengecek apakah file ada
if os.path.exists(nama_file):
    konfirmasi = input(f"Anda yakin ingin menghapus '{nama_file}'? (y/n): ").lower()
    if konfirmasi == "y":
        os.remove(nama_file)
        print(f"File '{nama_file}' berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")
else:
    print(f"File '{nama_file}' tidak ditemukan.")
