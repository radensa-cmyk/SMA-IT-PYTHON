nama_buah = "Mangga"
# "Untuk setiap 'huruf' di dalam string 'nama_buah'..."
for huruf in nama_buah:
 print(f"Karakter saat ini: {huruf}")

 teman_teman = ["Budi", "Ani", "Charlie", "Dian"]
for teman in teman_teman:
 print(f"Selamat Tahun Baru, {teman}!")
print("Selesai!")

# Akan menghasilkan urutan 0, 1, 2, 3, 4
print("Menghitung dari 0 sampai 4:")
for i in range(5):
 print(i)

# Menghasilkan urutan 5, 6, 7
print("Menghitung dari 5 sampai 7:")
for i in range(5, 8):
 print(i)

 # Mencetak angka genap dari 2 sampai 10
print("Bilangan genap dari 2 sampai 10:")
for i in range(2, 11, 2):
 print(i) # Output: 2, 4, 6, 8, 10
# Menghitung mundur
print("Hitung mundur dari 5:")
for i in range(5, 0, -1):
 print(i) # Output: 5, 4, 3, 2, 1

 