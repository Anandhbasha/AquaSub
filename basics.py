# print
'''Hello
jhhjkm.m,.m.,
,,l,l,;l,;l,;l,l,'''
# print('Welcome to Python')
# print('Hello' ,'Every', 'one', sep='-',end="\t")
# # sep
# print("2000","02","22", sep='/' )
# Data Types
#Don't use Special Characters
#Case Sensitive
#variable name should be start with Letters only
#Variable name should not contain - or space

    # int    
    # float
    # string
    #boolean

# a=100
# b='50.2'
# name= "xyz"
# isalive = True

# print(type(a))
# print(type(b))
# print(type(name))
# print(type(isalive))

# operators
    #arithmetic operators
    # +,-,/,*.%,=,**
# print(2+2*(5+2))
    
# print(2**4)
# #logical operator
#     # and , or not,not equal
# a=10
# b=20
# # print(a<b and b>a)
# print(a<b or b<a)
# print(not(a<b))
# print(a!=b)

# #argument assignment operator
#     # =,+=,*=,-=,/=
# c=50
# # c=c+10
# c+=10
# c*=5
# print(c)
# # Membership operator
# name = "arun"
# print('k' in name)
# #identity
# a=50
# b=260
# print(a is b)

# a,b,c,d = 10,"names",True,10.5
# print(a,b,c,d)

# temp=a
# a=b
# a=temp
# print(a,b)
# a,b=b,a
# print(a,b)

#input

# userName = input("Enter Your name")
# print("Welcome", userName )

# length = float(input("Please Enter the length value:"))
# width = float(input("Please Enter the width value:"))
# width = float(input())
# area = length * width
# print(area)

##Complex data types
    # list(value can change),tuple(unable to change the value),range(start,end,increment) - order wise 
# listing = [100,200,300,400]
# print(listing[-1])
# listing[2]="Hello"
# print(listing)
# # tuple
# values = ("yamaha",2012,"cjks895222121")
# print(values)
# # ranging = range(10.5,12.5,0.2)
# # print(list(ranging))
# # values[0] = "Hero"
# # print(values)
#     # set,dictionary
# sets = {100,100,150,200,150}
# print(sets)


modelNumber = {
    "modelYear":2000,
    "modelName":"Honda",
    "model_type":"passion",
    }

modelNumbers = [
    {
    "modelYear":2000,
    "modelName":"Honda",
    "model_type":"Unicorn",
    }
]
newModel = {
    "modelYear":2010,
    "modelName":"Hero",
    "model_type":"passion",
}
newModel["model"] = "jhhkhh"
del newModel["modelYear"]
print(newModel)
modelNumbers.append(newModel)
print(modelNumbers)
print(modelNumber["model_type"])

# if
age = 10
if age>=18:
    print("The are adult")
elif age<10 and age<=18:
    print("He is Teenager")
else :
    print("He is child")


text = input("Enter the text")

reversed = text[::-2]

# : start point from last value
#: end point upto first value
#-1 minius the index value position

print(text)
print(reversed)

if reversed==text:
    print("Palindrome")
else:
    print("Not a Palindrome")


lists = ["ndjknkj4411444","jkjjk1524752","jkjjk1524745454"]

# Hello
    # -1=0
    # -2=l