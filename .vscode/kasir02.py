# Kasir 
#Cerdas  2.0- Abu Musa Alasyary

# Fungsi Header
def tampilkan_header():
    print("="*40)
    print(" SELAMAT DATANG DI RADENSA STORE")
    print("="*40)

# Fungsi hitung subtotal
def hitung_subtotal(daftar_harga, daftar_jumlah):
    total = 0
    for i in range(len(daftar_harga)):
        total += daftar_harga[i] * daftar_jumlah[i]
    return total

# Fungsi hitung diskon
def hitung_diskon(subtotal):
    if subtotal >= 500000:
        persen = 10
    elif subtotal >= 300000:
        persen = 5
    else:
        persen = 0
    diskon = subtotal * (persen / 100)
    return diskon, persen

# Fungsi tampilkan struk
def tampilkan_struk(nama, harga, jumlah, subtotal, total_diskon, persen_diskon):
    print("="*40)
    print(" STRUK PEMBELIAN ANDA")
    print("="*40)
    print("Detail Belanja:")
    for i in range(len(nama)):
        total = harga[i] * jumlah[i]
        print(f"{i+1}. {nama[i]} ({jumlah[i]} x Rp {harga[i]:,.2f}) = Rp {total:,.2f}")
    print("-"*40)
    print(f"Subtotal       : Rp {subtotal:,.2f}")
    print(f"Diskon ({persen_diskon}%) : - Rp {total_diskon:,.2f}")
    print("-"*40)
    print(f"Total bayar    : Rp {subtotal - total_diskon:,.2f}")
    print("="*40)
    print(" TERIMA KASIH TELAH BERBELANJA!")
    print("="*40)

# Fungsi input valid
def get_numeric_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

# Program utama

# Inisialisasi data belanja
nama_barang = []
harga_barang = []
jumlah_barang = []

# Tampilkan header
tampilkan_header()

print("--- Masukkan Detail Barang ---")
print("(Ketik 'selesai' untuk mengakhiri input)")

while True:
    nama = input("Nama Barang: ")
    if nama.lower() == 'selesai':
        break

    harga = get_numeric_input("Harga Satuan (Rp): ")
    jumlah = get_numeric_input("Jumlah: ")

    nama_barang.append(nama)
    harga_barang.append(harga)
    jumlah_barang.append(jumlah)
    print("--- Barang berhasil ditambahkan! ---")

# Hitung subtotal dan diskon
subtotal = hitung_subtotal(harga_barang, jumlah_barang)
diskon, persen = hitung_diskon(subtotal)

# Cetak struk
print("\nMenghitung total belanja Anda...")
tampilkan_struk(nama_barang, harga_barang, jumlah_barang, subtotal, diskon, persen)
