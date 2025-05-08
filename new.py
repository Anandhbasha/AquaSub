# User-defined Functions, Return, Parameters |
def name():
    print("Hello")
name()

def add(a,b):
    return a+b

print(add(20,40))
# Lambda, *args, **kwargs, Variable Scope, Closures |

double = lambda x,y: x*y


print(double(10,50))

argus = lambda *args:print(args)
argus(10,20,50,40,60,80)


# objects = lambda **kwargs:
#     for key,value in kwarg
# def users(**kwargs):
#     for key,value in kwargs.items():
#         print(f'{key}:{value}')
# users(name="xyz",age=30)

# def outfunc(msg):
#     def innerfunc():
#         print(msg)
#     return innerfunc
# closer = outfunc("Hello,Guys")
# closer()

# Object-Oriented Concepts – Class, Object, Attributes |

# class students:
#     def stu(self):
#         print("This is stud name")
#     def res(self):
#         print("Second function")

# stud = students()
# # stud.stu()
# stud.res()

# class students:
#     def __init__(self,name,age,city):        
#         self.name=name
#         self.age=age
#         self.city=city
#     def details(self):
#         print(f'StudentName is {self.name} age is{self.age} city is {self.city}')

# stud = students("xyz",20,"cbe")
# stud.details()
        



# Inheritance, Composition, Method Overriding |

# class advisor:
#     def teacher(self):
#         print("This is Teacher")
# class student(advisor):
#     def stu(self):
#         print("This is student")


# s= student()
# s.stu()
# s.teacher()

# class Advisor:
#     def teacher(self):
#         print("This is Teacher")

# class Student:
#     def __init__(self):
#         self.students = Advisor()  
    
#     def out(self):
#         self.students.teacher()

# o = Student()
# o.out()



class Advisor:
    def teacher(self):
        print("This is Teacher")

class Student(Advisor):    
    def teacher(self):
        print("This is Student")

c=Student()
c.teacher()
