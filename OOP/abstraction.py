# Abstraction means displaying only basic information and hiding the details. Data abstraction refers to providing only necessary information about the data to the outside world, hiding the background info or implementation.

# import math
# print(pow(2,3)) #abstraction by header file

class Student:
    # def __init__(self):
    #     pass
    def __init__(self):
        print("Object Created")
    def display(self,x):
        print("wellcome",x)
        
s1=Student()
s1.display("ABhijite")