import time
import threading

def calcSquare(numbers):
    for i in numbers:
        time.sleep(0.2)
        print(f"Square {i}:{i*i}")

def calcCube(numbers):
    for i in numbers:
        time.sleep(0.2)
        print(f"Cube {i}:{i*i*i}")


t=time.time()

inpNum=[2,3,4,5]

t1=threading.Thread(target=calcSquare,args=(inpNum,))
t2=threading.Thread(target=calcCube,args=(inpNum,))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"program took {time.time()-t}")
