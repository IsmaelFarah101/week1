class Student:
    def __init__(self, name, college_id, gpa):
        self.name = name
        self.college_id = college_id
        self.gpa = gpa

    ##this is usefull method in python classes that prints useful information when teh user prints the class instance
    def __str__(self):
        return f'Name: {self.name}, id: {self.college_id} gpa: {self.gpa}'

student = Student('ismael',"123e1ee2d",'4')
print(student)