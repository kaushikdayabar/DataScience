class AdultException(Exception):
    pass


class Person:

    def __init__(self,name,age):
        self.PName=name
        self.PAge=age

    def get_minor_age(self):
        if self.PAge>18:
            raise AdultException

        else:
            print(self.PAge)

    def display_Person(self):
        try:
            self.get_minor_age()
        except AdultException:
             print("He is Major")
        finally:
            print(f"Name={self.PName} and Age={self.PAge}")

ob=Person("Raji",89)
ob.display_Person()

ob1=Person("Rajiv",17)
ob1.display_Person()
