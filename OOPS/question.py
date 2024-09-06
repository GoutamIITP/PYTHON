'''Createstudent class that takes name & marks of 3 subjects ,
as arguments in constructor. Then create a method to print the average.'''

class student:
    def  __init__(self, name, maths, science, english):
        self.name = name
        self.maths =  maths
        self.science =  science
        self.english = english

    def average(self):
        avg = (self.maths + self.science + self.english) / 3
        return print(f"The average marks of {self.name} is {avg}")

        
s1 = student("Karna", 99, 98, 97)
s1.average()

s1.name = "Ganna"
s1.average()

# Method 2 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(f"hi, {self.name} your avg score is:{sum / 3}")

s2 = Student("Arjun", [40, 50, 90])
s2.get_avg()