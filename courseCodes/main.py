vize = int(input("Vize notunuzu giriniz: "))
final = int(input("Final notunuzu giriniz: "))
ortalama = (vize * 0.4) + (final * 0.6)

# eğer final 40'dan küçükse kullanıcı kaldı
# eğer ortalama 50'den küçükse kullanıcı kaldı
# eğer vize finalin 2 katı ise kullanıcı kaldı
# bunun dışındaki tüm durumlarda kullanıcı geçti yazdırmak istiyoruz.

# if (final < 40):
#     print("Final 40'ın altında olduğu için kaldınız")
# elif (ortalama < 50):
#     print("Ortalama 50 altında olduğundan dolayı kaldınız")
# elif (vize == final * 2):
#     print("Kaldı")
# else:
#     print("Geçti")

# ANOTHER WAY
if final < 40 or ortalama < 50 or vize == final * 2:
    print("Kaldı")
else:
    print("Geçti")
# karar yapıları -end
