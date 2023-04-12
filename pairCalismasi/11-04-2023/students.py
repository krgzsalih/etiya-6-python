class Student:
    name = ""
    occupasion = ""

    def __init__(self, name, occupasion="student"):
        self.name = name
        self.occupasion = occupasion

    def __str__(self) -> str:
        return f"{self.occupasion} -> {self.name}"

    def talks(self):
        print(f"{self.name} is talking")

    def knows(self, subject):
        print(f"{self.name} knows this subject : {subject}")


# one = Student("ahmet", "Student")
# one.talks()
# one.knows("Computer science")
