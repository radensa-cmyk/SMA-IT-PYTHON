# kucing oyen

class Kucing:
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna

    def bersuara(self):
        print("Meow!")

    def perkenalkan_diri(self):
        print(f"Halo, saya kucing bernama {self.nama} dan warna saya {self.warna}.")


# object dari class Kucing
kucing1 = Kucing("Oren", "Oranye")
kucing2 = Kucing("Milo", "Coklat")

# manggil method  masing-masing object
kucing1.perkenalkan_diri()
kucing1.bersuara()

kucing2.perkenalkan_diri()
kucing2.bersuara()
