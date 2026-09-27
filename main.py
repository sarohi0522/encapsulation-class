class MyClass:
    __privateVar = 26
    def __privateMeth(self):
        print("Hi I am in a private method")

    def Hello(self):
        print("Private variable value is: ", MyClass.__privateVar)

obj = MyClass()
obj.Hello()
obj.__privateMeth()