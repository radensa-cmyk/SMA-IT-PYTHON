
import re
data = "Pendapatan bulan ini adalah Rp 1,500,000, sedangkan pengeluaran sebesar Rp 850,000."
hasil = re.findall(r'\d+', data)
print(hasil)  
