class Person:
    def __init__(self, Name):
        self.Name = Name
    def __str__(self):
        return self.Name

    def activity(self):
        raise NotImplementedError


class PresidentOfUkraine(Person):

    def activity(self):
        print("Krosavcheg")


class ChiefCommander(Person):

    def activity(self):
        print("ZSU")


class rusnya(Person):

    def activity(self):
        print("Looser")


NAMES = [PresidentOfUkraine("Zelenskiy"), ChiefCommander("Zaluzhniy"), rusnya("putin")]

for name in NAMES:
    print(name, end=" ")
    name.activity()

