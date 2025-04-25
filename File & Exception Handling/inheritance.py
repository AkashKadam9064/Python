class Base1:
    def __init__(self):
        print("This is init() method of Base1.")

    def show_base1(self):
        print("Base1")

class Base2:
    def show_base2(self):
        print("Base2")

class Derived1(Base1, Base2):
    def show_derived1(self):
        print("This is Derived class show() method.")

class Derived2(Derived1):
    pass

if __name__ == "__main__":
    obj = Derived2()
    obj.show_base1()
    obj.show_base2()
    obj.show_derived1()
