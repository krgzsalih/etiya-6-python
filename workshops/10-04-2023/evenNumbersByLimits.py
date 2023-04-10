def evenNumbersByLimits():
    lowerLimit = int(input("Alt limit giriniz : "))
    upperLimit = int(input("Üst limit giriniz : "))
    numberList = []
    for i in range(lowerLimit, upperLimit):
        if (i % 2 == 0):
            numberList.append(i)
    print(numberList)


evenNumbersByLimits()
