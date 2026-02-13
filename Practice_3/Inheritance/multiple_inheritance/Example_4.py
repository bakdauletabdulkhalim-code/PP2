class Mugalim:
    def oqytu(self):
        print("Sabak berdi")

class Sportshy:
    def zhattygu(self):
        print("Zhattygu jasady")

class Ustaz(Mugalim, Sportshy):
    pass

u = Ustaz()
u.oqytu()
u.zhattygu()
