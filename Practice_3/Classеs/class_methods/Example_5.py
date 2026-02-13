class Kitap:
    def __init__(self, aty, bagasy):
        self.aty = aty
        self.bagasy = bagasy

    def __str__(self):
        return f"Kitap: {self.at}, Bagasy: {self.bagasy}"

k1 = Kitap("Python", 5000)
print(k1)
