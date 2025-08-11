# Fungsi untuk membuat email dengan domain default
def buat_email(nama_pengguna, domain="coding.com"):
    email = f"{nama_pengguna.lower()}@{domain.lower()}"
    return email

# Contoh pemanggilan fungsi
print(buat_email("Budi"))             # Output: budi@coding.com
print(buat_email("Ani", "belajar.id"))  # Output: ani@belajar.id

#2
def kirim_paket(barang, tujuan, berat_kg, asuransi=False, express=False):
    print(f"Mengirim {barang} ke {tujuan} dengan berat {berat_kg} kg.")
    if asuransi:
        print("Paket diasuransikan.")
    if express:
        print("Menggunakan layanan express.")
    print("Pengiriman berhasil!")

# Memanggil fungsi dengan keyword arguments
kirim_paket(barang="sapi", tujuan="peternakan", berat_kg=950, express=True)

def analisis_daftar(daftar_angka):
    """
    Menganalisis daftar angka dan mengembalikan jumlah total, jumlah elemen, dan nilai rata-rata.

    Args:
        daftar_angka (list): Daftar angka yang akan dianalisis.

    Returns:
        tuple: (jumlah_total, jumlah_elemen, rata_rata)
    """
    jumlah_total = sum(daftar_angka)
    jumlah_elemen = len(daftar_angka)
    rata_rata = jumlah_total / jumlah_elemen
    return jumlah_total, jumlah_elemen, rata_rata

# Panggil fungsi dan "unpack" hasilnya
data = [10, 20, 30, 40, 50]
total, jumlah, rata_rata = analisis_daftar(data)

# Cetak hasilnya
print(f"Daftar angka: {data}")
print(f"Jumlah total: {total}")
print(f"Jumlah elemen: {jumlah}")
print(f"Nilai rata-rata: {rata_rata}")

#4.


def analisis_daftar(daftar_angka):
    """
    Menganalisis daftar angka untuk menghitung nilai minimum, maksimum, dan rata-rata.

    Fungsi ini menerima sebuah daftar berisi angka dan mengembalikan tiga nilai:
    angka terkecil, angka terbesar, dan rata-rata dari semua angka dalam daftar.

    Args:
        daftar_angka (list): Sebuah daftar (list) yang berisi angka-angka (int atau float).

    Returns:
        tuple: Sebuah tuple yang berisi tiga nilai:
               - min_val (int/float): Nilai terkecil dalam daftar.
               - max_val (int/float): Nilai terbesar dalam daftar.
               - avg_val (float): Rata-rata dari semua nilai dalam daftar.
               Mengembalikan (None, None, None) jika daftar kosong.
    """
    if not daftar_angka:
        return None, None, None

    min_val = min(daftar_angka)
    max_val = max(daftar_angka)
    avg_val = sum(daftar_angka) / len(daftar_angka)

    return min_val, max_val, avg_val

# Memanggil help() untuk memeriksa docstring
help(analisis_daftar)




# Fungsi asli (sebagai referensi)
# def get_luas_lingkaran(radius):
#     return 3.14159 * (radius ** 2)

# Mengubah fungsi menjadi lambda expression
luas_lingkaran_lambda = lambda radius: 3.14159 * (radius ** 2)

# Menguji lambda expression
radius_uji = 5
luas = luas_lingkaran_lambda(radius_uji)
print(f"Luas lingkaran dengan radius {radius_uji} adalah: {luas}")

radius_uji_lain = 10
luas_lain = luas_lingkaran_lambda(radius_uji_lain)
print(f"Luas lingkaran dengan radius {radius_uji_lain} adalah: {luas_lain}")

