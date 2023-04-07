number = int(input("Lütfen bir sayı giriniz : "))
total = 0
for i in range(1, number):
    if (number % i == 0):
        total += i

if (total == number):
    print(f"{number} sayısı mükemmel sayıdır.")
else:
    print(f"{number} sayısı mükemmel değildir.")
