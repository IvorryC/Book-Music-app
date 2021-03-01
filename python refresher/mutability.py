from typing import List, Optional


class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None): #This is the problem, now its fixed!
        self.name = name 
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student("Bob") 
rolf = Student("rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)