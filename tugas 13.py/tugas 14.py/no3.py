
kalimat = input("Masukkan sebuah kalimat: ")
kata_kata = kalimat.split()
jumlah_kata = len(kata_kata)
print("Jumlah kata:", jumlah_kata)
kata_kata.sort()
print("Kata-kata terurut:", kata_kata)

# Sing penting:
# split() → mecah kalimat dadi kata.
# len() → ngitung jumlah kata.
# sort() → ngurutno kata miturut abjad.