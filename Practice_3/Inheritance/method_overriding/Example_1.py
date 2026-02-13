class Habar:
    def jiberu(self):
        print("Habar jiberildi")

class Email(Habar):
    def jiberu(self):
        print("Email jiberildi")

h1 = Habar()
e1 = Email()

h1.jiberu()
e1.jiberu()
