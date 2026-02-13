class Surak:
    def soileu(self):
        print("Soiledi")

class Zhumys:
    def isteu(self):
        print("Zhumys istedi")

class Robot(Surak, Zhumys):
    pass

r = Robot()
r.soileu()
r.isteu()
