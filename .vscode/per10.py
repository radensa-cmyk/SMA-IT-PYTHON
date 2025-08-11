judul = input("Masukkan judul buku: ")
judul_bersih = judul.strip().title()  # Hilangkan spasi ekstra dan ubah ke Title Case
print("Judul yang sudah distandarisasi:", judul_bersih)


#2
email = input("Masukkan alamat email: ")

if "@" in email and (email.endswith(".com") or email.endswith(".co.id")):
    print("Email valid")
else:
    print("Email tidak valid")

#3
kalimat = input("Masukkan kalimat: ")
kata_sensor = input("Masukkan kata yang ingin disensor: ")

kalimat_sensor = kalimat.replace(kata_sensor, "***")
print("Kalimat setelah disensor:", kalimat_sensor)

#4
nama_organisasi = input("Masukkan nama organisasi: ")
kata_kata = nama_organisasi.split()  # Pecah menjadi list kata
akronim = ""

for kata in kata_kata:
    akronim += kata[0].upper()

print("Akronim:", akronim)

#5
import re

judul = input("Masukkan judul artikel: ")
slug = judul.lower().replace(" ", "-")  # Huruf kecil dan ganti spasi dengan tanda hubung
slug = re.sub(r'[^a-z0-9\-]', '', slug)  # Hapus karakter selain huruf, angka, tanda hubung

print("Slug URL:", slug)
