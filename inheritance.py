class Parent:
    def phone(self):
        print("Samsung 150")
    def bike(self):
        print("Passion pro")


class Child(Parent):
    def phone(self):
        print("iphone 12")

ch=Child()
# over riding
ch.phone()
# overloading
ch.bike()