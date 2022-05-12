class MainClass:
    def InstanceMethod(self):
        print(f'Calling instance method of class {self}')

    @classmethod
    def ClassMethod(cls):
        print(f'Calling class method of {cls}')

    @staticmethod
    def StaticMethod():
        print("Calling Static method.")


# Calling Instance Method
mainClass = MainClass()
mainClass.InstanceMethod()
MainClass.InstanceMethod(mainClass)

# Calling Class Method
MainClass.ClassMethod()

# Calling Static Method
MainClass.StaticMethod()
