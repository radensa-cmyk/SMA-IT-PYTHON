def salam_pembuka():
  """
  Fungsi ini mencetak pesan selamat datang sederhana.
  """
  print("==============================")
  print("Selamat Datang di Program Saya!")
  print("==============================")

# Memanggil fungsi beberapa kali
salam_pembuka()
salam_pembuka()
salam_pembuka()


def info_cuaca(kota, cuaca):
  """
  Fungsi ini mencetak informasi cuaca untuk kota tertentu.

  Args:
    kota (str): Nama kota.
    cuaca (str): Kondisi cuaca.
  """
  print(f"Cuaca di kota {kota} hari ini {cuaca}.")

# Contoh pemanggilan fungsi:
info_cuaca("Jakarta", "berawan")
info_cuaca("Bandung", "cerah")
info_cuaca("Surabaya", "hujan")


def kubik(angka):
  """
  Fungsi ini menghitung dan mengembalikan hasil dari sebuah angka pangkat 3.

  Args:
    angka (int/float): Angka yang akan dipangkatkan 3.

  Returns:
    int/float: Hasil dari angka pangkat 3.
  """
  return angka ** 3

# Memanggil fungsi dengan angka 4
hasil_kubik = kubik(4)

# Mencetak hasil yang disimpan dalam variabel
print(hasil_kubik)

#.4
# Fungsi untuk menghitung diskon
def hitung_diskon(harga_awal, persen_diskon):
    jumlah_diskon = harga_awal * (persen_diskon / 100)  # Hitung jumlah diskon
    harga_akhir = harga_awal - jumlah_diskon            # Hitung harga akhir
    return harga_akhir                                   # Kembalikan nilai harga akhir

# Meminta input dari pengguna
try:
    harga = float(input("Masukkan harga barang: "))
    diskon = float(input("Masukkan persen diskon (%): "))

    # Panggil fungsi dan tangkap hasilnya
    harga_setelah_diskon = hitung_diskon(harga, diskon)

    # Tampilkan hasil
    print(f"Harga setelah diskon: {harga_setelah_diskon:.2f}")
except ValueError:
    print("Error: Input harus berupa angka.")


    #5.

    # Fungsi untuk mengonversi Fahrenheit ke Celsius
def fahrenheit_ke_celsius(temp_f):
    celsius = (temp_f - 32) * 5 / 9
    return celsius

# Memanggil fungsi dengan nilai 98.6
hasil = fahrenheit_ke_celsius(98.6)

# Mencetak hasil konversi
print(f"Hasil konversi: {hasil:.2f}°C")

