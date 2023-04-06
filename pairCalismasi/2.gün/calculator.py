print("1. Sayıyı giriniz :")
sayi1 = int(input())
print("2. Sayıyı giriniz :")
sayi2 = int(input())

print("Lütfen yapmak istediğiniz işlemin numarasını seçiniz: 1-Toplama, 2-Çıkarma, 3-Çarpma, 4-Bölme")
enteredOperator = int(input())
sonuc = 0
if (enteredOperator == 1):
    sonuc = sayi1 + sayi2
elif (enteredOperator == 2):
    sonuc = sayi1 - sayi2
elif (enteredOperator == 3):
    sonuc = sayi1 * sayi2
elif (enteredOperator == 4):
    if (sayi2 != 0):
        sonuc = sayi1 / sayi2
    else:
        print("Sayı sıfıra bölünemez!")
else:
    print("Geçersiz işlem numarası!")


print("Sonuç :", sonuc)
