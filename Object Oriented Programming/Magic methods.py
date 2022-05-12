class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hello, {self.name} is {self.age} year(s) old."

    def __repr__(self):
        return f"<Person('{self.name}',{self.age})>"

john = Person("John",23)
print(john)