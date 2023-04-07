# Kullanıcıdan 10 adet sayı alalım ve bu sayılar arasından en büyük olanı kullanıcıya gösterelim.

numberList = []
for i in range(10):
    number = int(input("Sayı giriniz : "))
    numberList.append(number)
# numberList.sort()
print(numberList)
print("Dizideki en büyük sayı : ", max(numberList))
