from dataclasses import dataclass


##this is a decorator that python of formating your class for storing the state  
@dataclass
class Student:
    name: str
    college_id: int

def main():
    john = Student('John',1344566)
    jacob = Student('Jacob', 1277641)
    print(john)
    print(jacob)

main()