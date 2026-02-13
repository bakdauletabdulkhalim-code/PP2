class Tauar:
    def __init__(self, aty):
        self.aty = aty

class Telefon(Tauar):
    def habar(self):
        print(self.aty, "satylymda bar")

t1 = Telefon("iPhone")
t1.habar()
