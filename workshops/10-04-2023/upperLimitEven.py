def upperLimitEven():
    upperLimit = int(input("Üst limit giriniz : "))
    numberList = []
    for i in range(0, upperLimit, 2):
        numberList.append(i)
    print(numberList)


upperLimitEven()
