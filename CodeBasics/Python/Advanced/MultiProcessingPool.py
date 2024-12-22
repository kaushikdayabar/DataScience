from multiprocessing import Pool
import time
def add100Func(n):
    for i in range(100):
        time.sleep(0.05)
        n=n+1
    return n

if __name__=="__main__":
    t1=time.time()
    arr=[1,2,3]
    res=[]

    """ 
    Serial Processing
    for i in arr:
        res.append(add100Func(i))
    """
    #Parallel Processing using Map and Reduce
    print(type(Pool))
    p=Pool()
    """
    map method takes 2 parameters
    1.Function
    2.Array to operate on
    """
    res=p.map(add100Func,arr)

    print(res)
    t2 = time.time()
    print("Time Taken seconds",t2-t1)
