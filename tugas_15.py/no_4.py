kalimat = input("Masukkan sebuah kalimat: ").lower()
kata_kata = kalimat.split()

histogram = {}
for kata in kata_kata:
    histogram[kata] = histogram.get(kata, 0) + 1

print("Histogram kata:", histogram)
