class Adam:
    def __init__(self, aty, tegi):
        self.aty = aty
        self.tegi = tegi

class Student(Adam):
    def __init__(self, aty, tegi):
        super().__init__(aty, tegi)
        self.bitisu_jyly = 2024

s1 = Student("Dias", "Kali")
print(s1.aty, s1.bitisu_jyly)
