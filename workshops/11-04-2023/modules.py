# alias
import matematik as m
# sadece bir fonks çağırmak istiyorsak
from matematik import topla as toplamaIslemi

from classlar import Human

# built-in random int üretir
import random

toplama = m.topla(10, 51)
print(toplama)

bolme = m.bolme(10, 2)
print(bolme)

print(random.randint(0, 10))

print(toplamaIslemi(10, 11))

newHuman = Human("Muhittin")
newHuman.talk("Hello")
