class Base:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        print(f"Area of rectangle is {self.length * self.breadth:.2f}")

class Derived(Base):
    def area(self):
        super().area()
        print(f"Area of circle is {3.14 * self.length * self.length:.2f}")

if __name__ == '__main__':
    obj = Derived(10, 20)
    obj.area()

