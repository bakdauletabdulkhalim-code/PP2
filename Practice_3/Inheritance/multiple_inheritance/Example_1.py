class hello:
    def salem(self):
        print("Salem!")

class bye:
    def qosh(self):
        print("Qosh bol!")

class amandasu(hello, bye):
    pass

b = amandasu()
b.salem()
b.qosh()
