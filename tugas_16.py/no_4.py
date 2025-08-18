# Membaca file dan membuat histogram hari
filename = "mbox-short.txt"
try:
    with open(filename) as file:
        frekuensi_hari = {}
        for line in file:
            if line.startswith("From "):
                kata = line.split()
                hari = kata[2]  # kata ketiga = hari
                frekuensi_hari[hari] = frekuensi_hari.get(hari, 0) + 1

        print("Frekuensi pesan per hari:", frekuensi_hari)
except FileNotFoundError:
    print(f"File {filename} tidak ditemukan.")
