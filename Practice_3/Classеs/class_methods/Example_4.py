class Adam:
    def __init__(self, esim, jas):
        self.esim = esim
        self.jas = jas

    def jas_artu(self):
        self.jas += 1
        print(f"{self.at} qazir {self.jas} jasta")

a1 = Adam("Dias", 20)
a1.jas_artu()
a1.jas_artu()
