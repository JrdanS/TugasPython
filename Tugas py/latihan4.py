mhs = [
    [10121001, "Asep"],
    [10121002, "Budi"],
    [10121003, "Cecep"]
]

Nilai = [
    [10121001, 50, 70, 40, 80],
    [10121002, 78, 78, 80, 65],
    [10121003, 57, 88, 67, 69]
]

rata_mhs = []
for n in Nilai:
    rata = sum(n[1:]) / (len(n) - 1)
    rata_mhs.append(rata)

nilai_tertinggi = max(rata_mhs)
indeks_pintar = rata_mhs.index(nilai_tertinggi)
nama_pintar = mhs[indeks_pintar][1]

rata_mk = []
jumlah_mhs = len(mhs)
jumlah_mk = len(Nilai[0]) - 1 

for j in range(1, jumlah_mk + 1): 
    total_per_mk = 0
    for i in range(jumlah_mhs):
        total_per_mk += Nilai[i][j]
    rata_mk.append(total_per_mk / jumlah_mhs)


nilai_terkecil_mk = min(rata_mk)
indeks_mk = rata_mk.index(nilai_terkecil_mk)
nama_mk = f"MK{indeks_mk + 1}"

print(f"Mahasiswa Terpintar: {nama_pintar}(Nilai : {nilai_tertinggi:.2f})")
print(f"Mata Kuliah Nilai Terkecil : {nama_mk}(Nilai : {nilai_terkecil_mk:.2f})")