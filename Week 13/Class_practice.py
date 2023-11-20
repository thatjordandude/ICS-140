class Student:
    def __init__(self, first, last, gpa, school):
        self.first = first
        self.last = last
        self.gpa = gpa
        self.school = school

    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
student1 = Student('Richard', 'Scholar', 3.2, 'Michigan State')
student2 = Student('Test', 'User', 4.0, 'Admin school')

print(student1.gpa)
print(student2.school)

print(student1.fullname())
print(Student.fullname(student1))