# # User-defined Functions, Return, Parameters |
# def name():
#     print("Hello")
# name()

# def add(a,b):
#     return a+b

# print(add(20,40))
# # Lambda, *args, **kwargs, Variable Scope, Closures |

# double = lambda x,y: x*y


# print(double(10,50))

# argus = lambda *args:print(args)
# argus(10,20,50,40,60,80)


# # objects = lambda **kwargs:
# #     for key,value in kwarg
# # def users(**kwargs):
# #     for key,value in kwargs.items():
# #         print(f'{key}:{value}')
# # users(name="xyz",age=30)

# # def outfunc(msg):
# #     def innerfunc():
# #         print(msg)
# #     return innerfunc
# # closer = outfunc("Hello,Guys")
# # closer()

# # Object-Oriented Concepts – Class, Object, Attributes |

# # class students:
# #     def stu(self):
# #         print("This is stud name")
# #     def res(self):
# #         print("Second function")

# # stud = students()
# # # stud.stu()
# # stud.res()

# # class students:
# #     def __init__(self,name,age,city):        
# #         self.name=name
# #         self.age=age
# #         self.city=city
# #     def details(self):
# #         print(f'StudentName is {self.name} age is{self.age} city is {self.city}')

# # stud = students("xyz",20,"cbe")
# # stud.details()
        



# # Inheritance, Composition, Method Overriding |

# # class advisor:
# #     def teacher(self):
# #         print("This is Teacher")
# # class student(advisor):
# #     def stu(self):
# #         print("This is student")


# # s= student()
# # s.stu()
# # s.teacher()

# # class Advisor:
# #     def teacher(self):
# #         print("This is Teacher")

# # class Student:
# #     def __init__(self):
# #         self.students = Advisor()  
    
# #     def out(self):
# #         self.students.teacher()

# # o = Student()
# # o.out()



# class Advisor:
#     def teacher(self):
#         print("This is Teacher")

# class Student(Advisor):    
#     def teacher(self):
#         print("This is Student")

# c=Student()
# c.teacher()


# static Method

# class Number:
#     @staticmethod
#     def addition(a,b):
#         return a+b

# print(Number.addition(10,20))

# # Class Method
# class Balance:
#     AccBalance = 0
#     @classmethod
#     def accounts(cls,newbalance):
#         cls.AccBalance=newbalance


# Balance.accounts(400)
# print(Balance.AccBalance)


# class Balance:
#     def __init__(self,balance,accNo,Name):
#         self.__balance=balance
#         self.name=Name
#         self.accNO = accNo
#     def userInfo(self):
#         print(f'accNo:{self.accNO}Balance:{self.__balance}')

# Ba = Balance(400,53454564654,"xyz")
# print(Ba.__balance)
#  Operator Overloading 

# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance= balance
#     def __sub__(self,other):
#         return print(f'{self.balance-other.balance}')

# a1 = BankAccount("xyz",7000)
# a2 = BankAccount("abc",8000)

# total = a1-a2

# sub ,eq,mul,truediv,floordiv,mod,pow,ne,ge,le,gt,lt
# Creating & Using Modules
# import basics
# print(basics.add(10,20))


# # Packages
# from Python import One
# print(One.hello())
# # Search Path 
# import sys
# print(sys.path)
# sys.path.append(r"D:\Python")
# from news import greet
# greet()

# # try:
# # except:
# # else:
# # finally:

# try:
#     a=10
#     b=2
#     a/b==0
# except:
#     print("Unable to divide")
# else:
#     print("Success")
# finally:
#     print("Code has Been Completed")



