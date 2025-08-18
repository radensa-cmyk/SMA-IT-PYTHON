biodata = {
    "nama": "Abu Musa Alasyary",
    "umur": 17,
    "hobi": ["mendaki", "panjat tebing", "Olahraga"],
    "belum_menikah": False
}
#dictionar
print("Dictionary biodata:", biodata)
# vlue
print("Nama:", biodata["nama"])
print("Hobi pertama:", biodata["hobi"][0])


#2
biodata["kota"] = "bekasi"                   # tambahkan key "kota"
biodata["umur"] = biodata["umur"] + 1       # umur tahun depan
print("Dictionary setelah diperbarui:", biodata)
#3
# Akses menggunakan [] -> akan error jika key tidak ada
# print(biodata["pekerjaan"])  # ini error, jadi dikomentari
# Akses dengan .get()
print("Akses .get() tanpa default:", biodata.get("pekerjaan"))
#.get() + default
print("Akses .get() dengan default:", biodata.get("pekerjaan", "Pelajar"))

