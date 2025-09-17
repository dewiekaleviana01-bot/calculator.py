print("===== KALKULATOR SEDERHANA =====")
name = input("Kenalan dulu dong, nama kamu siapa?: ")
name2 = str(name)
print(f"Halo {name2}!!! Selamat mencoba program kalkulator dari aku;>")
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
print("Pilih operasi: + - * /")
operasi = input("Masukkan operasi: ")
print('JENG JENG JENG')

if operasi == "+":
    hasil = angka1 + angka2
    print("Hasilnya adalahh:", hasil)
elif operasi == "-":
    hasil = angka1 - angka2
    print("Hasilnya adalahh:", hasil)
elif operasi == "*":
    hasil = angka1 * angka2
    print("Hasilnya adalahh:", hasil)
elif operasi == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
        print("Hasilnya adalahh:", hasil)
    else:
        print("Error: Waduh nggak bisa dibagi 0 inimah")
else:
    print("Operasi tidak valid")