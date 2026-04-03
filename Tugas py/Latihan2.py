x = int(input("Masukkan jumlah hari: "))

tahun = x // 365
sisa  = x % 365
bulan = sisa // 30
hari  = sisa % 30

print(f"{x} hari = {tahun} tahun, {bulan} bulan, {hari} hari")