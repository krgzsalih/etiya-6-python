def largestNumber():
    numberList = []
    for i in range(10):
        number = int(input("Sayı giriniz : "))
        numberList.append(number)
    print(numberList)
    print("Dizideki en büyük sayı : ", max(numberList))


largestNumber()
