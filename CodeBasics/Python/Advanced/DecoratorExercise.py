"""
Create a decorator function to check that the argument passed to the function factorial is a non-negative integer:

Create a factorial function which finds the factorial of a number.

Use the decorator to decorate the factorial function to only allow factorial of non-negative integers.

example:

    factorial(1.354) : raise Exception or print error message
    factorial(-1) : raise Exception or print error message
    factorial(5) : 120
"""

def decoratorFunc(func):
    #decorator is a wrapper over another function
    def wrapper(*args,**kwargs):
        #args means normal function arguments, the arguments that are mapped to parameters based on position
        #print("arguments",args,"\nargument's type",type(args))
        #kwargs means keyword arguments, the one's that are mapped to parameters based on argument name
        #print("Keyword Arguments ",kwargs,"\n keyword argument's type",type(kwargs))

        #factorial argument
        varArg=args[0]

        if varArg<0:
            print("Negative Value")
        elif int!=type(varArg):
            print("Not an Integer")
        else:
            func(*args,**kwargs)

    return wrapper

@decoratorFunc
def factorial(n):
    f=1
    while n>0:
        f=f*n
        n-=1
    print(f)

for i in [-1,1.35,5]:
    factorial(i)
