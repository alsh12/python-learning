class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student("Johny", (90, 92, 93, 89, 91))
print('Student Name: %s' % student.name)
print('Student Grade: %s' % str(student.grades))
print('Student Average: %s' % student.average())
print(f"Student Grade {student.grades}")
