class Juru:
    def juru(self):
        print("Juru")

class Sekiru:
    def sekiru(self):
        print("Sekiru")

class Hero(Juru, Sekiru):
    pass

h = Hero()
h.juru()
h.sekiru()
