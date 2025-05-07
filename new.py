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

def outfunc(msg):
    def innerfunc():
        print(msg)
    return innerfunc
closer = outfunc("Hello,Guys")
closer()