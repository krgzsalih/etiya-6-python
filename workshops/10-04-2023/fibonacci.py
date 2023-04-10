def fibonacciListele():
    fibonacciList = [1, 1]
    for i in range(20):
        if (len(fibonacciList) < 20):
            added = fibonacciList[-1] + fibonacciList[-2]
            fibonacciList.append(added)
        else:
            break
    print(fibonacciList)


fibonacciListele()
