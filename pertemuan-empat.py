# Meminta input dari pengguna
jam_kerja = float(input("Masukkan jumlah jam kerja: "))
tarif_per_jam = float(input("Masukkan tarif per jam: "))

# Menghitung total upah
if jam_kerja <= 40:
    upah = jam_kerja * tarif_per_jam  # Tidak ada lembur
else:
    jam_normal = 40
    jam_lembur = jam_kerja - 40
    upah = (jam_normal * tarif_per_jam) + (jam_lembur * tarif_per_jam * 1.5)

# Menampilkan hasil
print("Pay:", upah)


2

 try:
     # Minta input dari pengguna
     jam_kerja = float(input("Masukkan jumlah jam kerja: "))
     tarif_per_jam = float(input("Masukkan tarif per jam: "))

     # Hitung upah termasuk lembur
     if jam_kerja <= 40:
         upah = jam_kerja * tarif_per_jam
     else:
         jam_normal = 40
         jam_lembur = jam_kerja - 40
         upah = (jam_normal * tarif_per_jam) + (jam_lembur * tarif_per_jam * 1.5)

     # Tampilkan hasil
     print("Pay:", upah)

 except ValueError: 
     # Jika input bukan angka
     print("Error, please enter input")


 #3. 
 try:
     # Meminta input skor dari pengguna
     skor = float(input("Masukkan skor antara 0.0 dan 1.0: "))

     # Validasi rentang skor
     if skor < 0.0 or skor > 1.0:
         print("Bad score")
     else:
         # Menentukan grade berdasarkan skor
         if skor >= 0.9:
             print("Grade: A")
         elif skor >= 0.8:
             print("Grade: B")
         elif skor >= 0.7:
             print("Grade: C")
         elif skor >= 0.6:
             print("Grade: D")
         else:
             print("Grade: F")

 except ValueError:
     # Menangani input yang bukan angka
     print("Error, please enter numeric input")


 #4. 
 # Nilai input simulasi (ubah-ubah nilainya untuk pengujian)
 tinggi_cm = 155
 usia = 11
 didampingi_ortu = True

 # Logika aturan masuk
 if tinggi_cm >= 150 and (usia > 12 or didampingi_ortu):
     print("Boleh Masuk")
 else:
     print("Tidak Boleh Masuk")
