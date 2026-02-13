class Avto:
    def __init__(self, marka, jyl):
        self.marka = marka
        self.jyl = jyl

    def info(self):
        return f"{self.marka} - {self.jyl} jyl"

a1 = Avto("Toyota", 2020)
print(a1.info())
