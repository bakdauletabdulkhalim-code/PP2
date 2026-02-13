class Telefon:
    def qonyrau(self):
        print("Qonyrau shalu")

class Kamera:
    def suret(self):
        print("Suretke tusiru")

class Smartfon(Telefon, Kamera):
    pass

s = Smartfon()
s.qonyrau()
s.suret()
