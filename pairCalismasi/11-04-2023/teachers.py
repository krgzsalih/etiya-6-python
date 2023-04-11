class Teachers:
    name = ""
    occupasion = ""
    myTeachersList = []

    def __init__(self):
        # self.name = name
        # print(f"{name}")
        pass

    def addTeacher(self, teacherInput):
        self.myTeachersList.append(teacherInput)
        pass

    def talks(self):
        print(f"{self.name} is talking")

    def knows(self, expertise):
        print(f"{self.name} knows this expertise : {expertise}")


# one = Teachers("salih", "Teacher")
# one.talks()
# one.knows("Computer science")
