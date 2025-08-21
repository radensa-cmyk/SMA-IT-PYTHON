# Latihan 2: Class RekeningBank

class RekeningBank:
    def __init__(self, nomor_rekening, nama_pemilik):
        self.nomor_rekening = nomor_rekening
        self.nama_pemilik = nama_pemilik
        self.saldo = 0  # saldo awal 0

    def lihat_saldo(self):
        print(f"Saldo saat ini: Rp{self.saldo}")

    def setor(self, jumlah):
        self.saldo += jumlah
        print(f"Berhasil setor Rp{jumlah}. Saldo baru: Rp{self.saldo}")

    def tarik(self, jumlah):
        if jumlah > self.saldo:
            print("anda terlalu miskin, Saldo tidak mencukupi!")
        else:
            self.saldo -= jumlah
            print(f"Berhasil tarik Rp{jumlah}. Saldo baru: Rp{self.saldo}")


rekening_radensa = RekeningBank("123456789", "radensa")

# Uji coba method
rekening_radensa.lihat_saldo()   #  1
rekening_radensa.setor(500000)   # 2
rekening_radensa.setor(200000)   # 3
rekening_radensa.tarik(100000)   
rekening_radensa.tarik(700000)   
rekening_radensa.lihat_saldo()   
