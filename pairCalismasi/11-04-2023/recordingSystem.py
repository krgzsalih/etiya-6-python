import students
import teachers

studentsList = students.Student.myStudentlist
teachersList = teachers.Teachers.myTeachersList
allList = [studentsList, teachersList]

# def addStudent():
#     studentInput = str(input("Öğrenci ismini giriniz : "))
#     studentsList.append(studentInput)


# def addTeacher():
#     teacherInput = str(input("Öğretmen ismini giriniz : "))
#     teachersList.append(teacherInput)


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
            newStudent = students.Student()
            newStudent.addStudent(str(input("Öğrenci ismini giriniz : ")))
        elif (userInput == "öğretmen"):
            newTeacher = teachers.Teachers()
            newTeacher.addTeacher(str(input("Öğretmen ismini giriniz : ")))
        else:
            print("Lütfen belirtilen mesleklerden birini giriniz!")
    elif (userChoice == "listele"):
        selectList = str(
            input("Hangi listeyi görmek istiyorsunuz ? Örn: Öğrenciler/Öğretmenler/Hepsi : "))
        selectList.lower()
        if (selectList == "öğrenciler"):
            print(
                f"Öğrenci listesi gösteriliyor : \n{studentsList}")
        elif (selectList == "öğretmenler"):
            print(f"Öğretmen listesi gösteriliyor : \n{teachersList}")
        elif (selectList == "hepsi"):
            print(f"Hepsi gösteriliyor : \n{allList}")
        else:
            print("Lütfen geçerli seçeneği giriniz.")
