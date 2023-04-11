class Student:
    name = ""
    occupasion = ""
    myStudentlist = []

    def __init__(self):
        pass

    def __str__(self) -> str:
        return self.name

    def addStudent(self, studentInput):
        self.myStudentlist.append(studentInput)

    def talks(self):
        print(f"{self.name} is talking")

    def knows(self, subject):
        print(f"{self.name} knows this subject : {subject}")


# one = Student("ahmet", "Student")
# one.talks()
# one.knows("Computer science")
