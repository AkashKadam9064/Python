class UnderAgeError(Exception):
    def __init__(self, age):
        self.age = age

    def error(self):
        try:
            if self.age < 18:
                raise UnderAgeError("You are not 18+")
            else:
                print("Ok. Access Granted!")
        except UnderAgeError as e:
            print("Access Denied.", e)

        finally:
            print("Ended.")

if __name__ == '__main__':
    obj = UnderAgeError(10)
    obj.error()

