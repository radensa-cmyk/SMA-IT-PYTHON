import re
teks = "python adalah bahasa yang menyenangkan, python mudah dipelajari."
cari1 = re.search(r'python', teks)     # re.search()
print("re.search():", cari1.group())
cari2 = re.findall(r'python', teks)      # re.findall()
print("re.findall():", cari2)
