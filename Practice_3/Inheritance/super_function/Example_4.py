class Adam:
    def __init__(self, aty, tegi):
        self.aty = aty
        self.tegi = tegi

class Student(Adam):
    def __init__(self, aty, tegi, jyl):
        super().__init__(aty, tegi)
        self.bitiru_jyly = jyl

    def qosh_keldin(self):
        print("Qosh keldin", self.aty, self.tegi, "-", self.bitiru_jyly)

s1 = Student("Aruzhan", "Bek", 2026)
s1.qosh_keldin()
