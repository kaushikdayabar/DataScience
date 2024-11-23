import time

def calcSquare(numbers):
    start=time.time()
    result=[]
    for i in numbers:
        result.append(i*i)
    print(result)
    end=time.time()

    print("Square took "+ str((end-start)*1000)+"milli seconds")

def calcCube(numbers):
    start=time.time()
    result=[]
    for i in numbers:
        result.append(i*i*i)
    print(result)
    end=time.time()
    print("Cube took "+ str((end-start)*1000)+"milli seconds")


arr=range(1,100000)
calcSquare(arr)
calcCube(arr)
