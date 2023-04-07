# Kullanıcının vereceği üst limit ile 0'dan bu üst limite kadar olan tüm 'çift' sayıları ekrana yazdıralım.

upperLimit = int(input("Üst limit giriniz : "))
numberList = []
for i in range(0, upperLimit, 2):
    numberList.append(i)
print(numberList)
