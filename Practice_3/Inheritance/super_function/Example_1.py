class Adam:
    def __init__(self, aty, tegi):
        self.aty = aty
        self.tegi = tegi

class Student(Adam):
    def __init__(self, aty, tegi):
        super().__init__(aty, tegi)

s1 = Student("Aruzhan", "Nurmukhamed")
print(s1.aty, s1.tegi)
