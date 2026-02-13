class Adam:
    def __init__(self, aty, tegi):
        self.aty = aty
        self.tegi = tegi

class Student(Adam):
    def __init__(self, aty, tegi, jyl):
        super().__init__(aty, tegi)
        self.bitiru_jyly = jyl

s1 = Student("Ali", "Serik", 2025)
print(s1.aty, s1.bitiru_jyly)
