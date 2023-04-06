vize = float(input("Vize notunuzu giriniz: "))
final = float(input("Final notunuzu giriniz: "))
ortalama = float((vize * 0.4) + (final * 0.6))
harfNotu = str

if (ortalama >= 0 and ortalama < 50):
    harfNotu = "FF"
elif (ortalama >= 50 and ortalama < 60):
    harfNotu = "DD"
elif (ortalama >= 60 and ortalama < 70):
    harfNotu = "CC"
elif (ortalama >= 70 and ortalama < 80):
    harfNotu = "BB"
elif (ortalama >= 80 and ortalama <= 100):
    harfNotu = "AA"
else:
    print("Geçersiz not")

print(" ")
print("Ortalamanız : ", ortalama)
print("Harf notunuz : ", harfNotu)
