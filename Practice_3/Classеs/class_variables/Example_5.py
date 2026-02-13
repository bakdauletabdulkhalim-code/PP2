class Bank:
    procent = 0.1   # 10%

    def __init__(self, aqsha):
        self.aqsha = aqsha

    def procentter(self):
        return self.aqsha + self.aqsha * Bank.procent

b1 = Bank(1000)
print(b1.procentter())
