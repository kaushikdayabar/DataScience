import time


def decoratorFunc(func):
    #it is wrapper over a function
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        print(result)
        end=time.time()
        print(func.__name__+" took "+ str((end-start)*1000)+"milli seconds")
       
    return wrapper
    

@decoratorFunc        
def calcSquare(numbers):
    
    result=[]
    for i in numbers:
        result.append(i*i)
    return result
    
@decoratorFunc
def calcCube(numbers):
    result=[]
    for i in numbers:
        result.append(i*i*i)
    return result


arr=range(1,100000)
calcSquare(arr)
calcCube(arr)
