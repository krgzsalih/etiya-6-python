from students import Student
from teachers import Teachers

studentsList = []
teachersList = []
allList = []


def addStudent(studentInput):
    studentsList.append(studentInput)


def addTeacher(teacherInput):
    teachersList.append(teacherInput)


while True:
    userChoice = str(
        input("Yapmak istediğiniz işlem nedir ? (Örn: Listele / Ekleme) , yada çıkış yapmak için 'q' ya basınız : "))
    userChoice.lower()
    if (userChoice == "q"):
        print("Çıkış yapılıyor...")
        break

    if (userChoice == "ekleme"):
        userInput = str(
            input("Eklemek istediğiniz kişinin mesleği nedir ? (Öğrenci/Öğretmen) : "))
        userInput.lower()
        if (userInput == "öğrenci"):
            studentInput = str(input("Öğrenci ismini giriniz : "))
            studentNew = Student(studentInput)
            addStudent(studentNew)
        elif (userInput == "öğretmen"):
            teacherInput = str(input("Öğretmen ismini giriniz : "))
            teacherNew = Teachers(teacherInput)
            addTeacher(teacherNew)
        else:
            print("Lütfen belirtilen mesleklerden birini giriniz!")
    elif (userChoice == "listele"):
        selectList = str(
            input("Hangi listeyi görmek istiyorsunuz ? Örn: Öğrenciler/Öğretmenler/Hepsi : "))
        selectList.lower()
        if (selectList == "öğrenciler"):
            print("Öğrenci Listesi gösteriliyor :")
            for i, studentsList in enumerate(studentsList, start=1):
                print(f"{i}-) {studentsList.name}")
        elif (selectList == "öğretmenler"):
            print("Öğretmen Listesi gösteriliyor :")
            for i, teachersList in enumerate(teachersList, start=1):
                print(f"{i}-) {teachersList.name}")
        elif (selectList == "hepsi"):
            allList = [*studentsList, *teachersList]
            print(f"Tüm listeler gösteriliyor : ")
            for i, allList in enumerate(allList, start=1):
                print(f"{i}-) {allList}")
        else:
            print("Lütfen geçerli seçeneği giriniz.")
