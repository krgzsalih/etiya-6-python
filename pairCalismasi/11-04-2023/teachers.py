class Teachers:
    name = ""
    occupasion = ""

    def __init__(self, name, occupasion="teacher"):
        self.name = name
        self.occupasion = occupasion

    def __str__(self) -> str:
        return f"{self.occupasion} -> {self.name}"

    def talks(self):
        print(f"{self.name} is talking")

    def knows(self, expertise):
        print(f"{self.name} knows this expertise : {expertise}")


# one = Teachers("salih", "Teacher")
# one.talks()
# one.knows("Computer science")
