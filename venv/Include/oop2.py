

class PiggySave:

    def __init__(self):
        self.money = 0

    def add(self,amount):
        self.money += amount

    def open(self):
        total = self.money
        self.money = 0
        return total

my_save = PiggySave()
your_save = PiggySave()

my_save.add(500)
my_save.add(500)

print(my_save.open())

print(your_save.open())