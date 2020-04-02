

class Circle:

    def __init__(self):

        self.radius = 10

    def show(self):
        print("show", self.radius)

c1 = Circle()

c2 = Circle()

print(c1)
print(c1.radius)
print(c2)
print(c2.radius)

c1.radius = 5
c1.show()

c2.radius = 10
c2.show()