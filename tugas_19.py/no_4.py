import re
kalimat = "Kucing, anjing, dan burung adalah hewan peliharaan."
hasil = re.findall(r'\w+g', kalimat)
print(hasil)
