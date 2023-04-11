class Human:
    name = "Ahmet"
    # built-in
    # contructor alanı
    # initialize

    def __init__(self, name):
        self.name = name
        print("Human instance üretildi")

    # -> str (geriye dönüş tipini belirtir)
    def __str__(self) -> str:
        return f"STR fonksiyonundan dönen değer: {self.name}"

    def talk(self, sentence):
        print(f"{self.name} : {sentence}")

    def walk(self):
        print(f"{self.name} is walking")

# instance => örnek
# self => this (bir class içinde tanımlanan fonksiyon için kullanmalıyız, rezerve parametredir)


human1 = Human("Salih")
human1.talk("Merhaba")
human1.walk()
print(human1)

human2 = Human("Tonyali")
human2.talk("selam")
human2.walk()
print(human2)
