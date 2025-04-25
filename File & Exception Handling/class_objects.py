class Base:
    def __del__(self):
        print("Destructor")

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Constructor Called")

    def show(self):
        print(f"My name is {self.name} and my age is {self.age}.")

if __name__ == '__main__':
    obj = Base("Akash", 23)
    obj.show()
