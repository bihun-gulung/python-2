#soal pertama: menentukan bilangan genap atau ganjil
angka = int(input("masukkan nilai: "))

if angka % 2 == 0:
    print(f"Hasil: {angka} adalah bilangan genap.")
elif angka % 2 == 1:
     print(f"Hasil: {angka} adalah bilangan ganjil.")
else:
    print(f"Bilangan yang anda masukkan bukan bilangan ganjil/genap.")

#soal kedua : perulangan while 
angka = int(input("masukkan nilai: "))
i = 1
jumlah = 0
while i <= angka:
    jumlah += i
    i += 1
    print("Jumlah=", jumlah)

#soal ketiga: tabel perkalian 
angka = int(input("masukkan nilai: "))
print(f"Tabel perkalian  {angka}:")
for i in range(1,11):
    hasil = angka * i
    print(f"{angka} x {i} = {hasil}")

