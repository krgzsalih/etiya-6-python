fibonacci = [1, 1]
fibonacci2 = [1, 1]

# first way
for i in range(20):
    if len(fibonacci2) < 20:
        next2 = fibonacci2[-1] + fibonacci2[-2]
        fibonacci2.append(next2)

print(fibonacci2)

# second way

while len(fibonacci) < 20:
    next = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next)

print(fibonacci)
