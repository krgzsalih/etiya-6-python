# Kullanıcının vereceği üst limit ile alt limiti belirlemesi için gerekli desteği ekleyelim.
# Bu üst limite kadar olan tüm 'çift' sayıları ekrana yazdıralım.

lowerLimit = int(input("Alt limit giriniz : "))
upperLimit = int(input("Üst limit giriniz : "))
numberList = []
for i in range(lowerLimit, upperLimit):
    if (i % 2 == 0):
        numberList.append(i)
print(numberList)
