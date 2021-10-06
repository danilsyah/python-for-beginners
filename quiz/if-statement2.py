'''algoritman lampu lalu lintas'''

# deklarasi
#  warna : 1. merah, 2. hijau, 3. kuning

print("-App Lampu Lalu Lintas-")
print("1. Merah")
print("2. Hijau")
print("3. Kuning")
warna = int(input("Masukan Warna Lampu dengan Angka : "))
if warna == 1:
    print("Berhenti")
elif warna == 2:
    print("Jalan")
elif warna == 3:
    print("Hati-hati")
else:
    print("pilihan tidak ada")

    """algoritma menentukan nilai indexs -prestasi
    """
nilaiAkhir = int(input("Masukan Nilai Akhir : "))
if nilaiAkhir >= 85:
    result = 'A'
elif nilaiAkhir < 85 and nilaiAkhir >= 70:
    result = 'B'
elif nilaiAkhir < 70 and nilaiAkhir >= 55:
    result = 'C'
elif nilaiAkhir < 55 and nilaiAkhir >= 40:
    result = 'D'
else:
    result = 'E'

print(result)
