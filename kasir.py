# Kasir Cerdas Sederhana + Bonus (PPN dan Kembalian)

print("=" * 43)
print("SELAMAT DATANG DI PROGRAM KASIR CERDAS!")
print("=" * 43)

# --- Input Barang 1 ---
print("\n--- Masukkan Detail Barang 1 ---")
nama_barang_1 = input("Nama Barang: ")
harga_1 = float(input("Harga Satuan (Rp): "))
jumlah_1 = int(input("Jumlah: "))

# --- Input Barang 2 ---
print("\n--- Masukkan Detail Barang 2 ---")
nama_barang_2 = input("Nama Barang: ")
harga_2 = float(input("Harga Satuan (Rp): "))
jumlah_2 = int(input("Jumlah: "))

print("\nMenghitung total...")

# --- Kalkulasi Total ---
total_1 = harga_1 * jumlah_1
total_2 = harga_2 * jumlah_2
subtotal = total_1 + total_2

# --- Logika Diskon ---
diskon = 0.0
persen_diskon = 0
if subtotal > 200_000:
    persen_diskon = 10
    diskon = 0.10 * subtotal
elif subtotal > 100_000:
    persen_diskon = 5
    diskon = 0.05 * subtotal

total_setelah_diskon = subtotal - diskon

# --- PPN 11% ---
ppn = 0.11 * total_setelah_diskon
total_final = total_setelah_diskon + ppn

# --- Pembayaran ---
uang_bayar = float(input("\nMasukkan jumlah uang yang dibayarkan (Rp): "))
kembalian = uang_bayar - total_final

# --- Cetak Struk ---
print("\n" + "=" * 43)
print(" STRUK PEMBELIAN ANDA")
print("=" * 43)
print("Detail Belanja:")
print(f"1. {nama_barang_1} ({jumlah_1} x Rp {harga_1}) = Rp {total_1}")
print(f"2. {nama_barang_2} ({jumlah_2} x Rp {harga_2}) = Rp {total_2}")
print("-" * 43)
print(f"Subtotal           : Rp {subtotal:,.2f}")
print(f"Diskon ({persen_diskon}%)     : - Rp {diskon:,.2f}")
print(f"Setelah Diskon     : Rp {total_setelah_diskon:,.2f}")
print(f"PPN (11%)          : + Rp {ppn:,.2f}")
print("-" * 43)
print(f"Total Akhir        : Rp {total_final:,.2f}")
print(f"Uang Dibayar       : Rp {uang_bayar:,.2f}")
print(f"Kembalian          : Rp {kembalian:,.2f}")
print("=" * 43)
print(" TERIMA KASIH TELAH BERBELANJA!")
print("=" * 43)