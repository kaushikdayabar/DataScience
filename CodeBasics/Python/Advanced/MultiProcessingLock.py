import multiprocessing
import time

def deposit(dep,Bal):
    for i in range(dep):
        time.sleep(0.1)
        Bal.value=Bal.value+1

def withdraw(withdraw,Bal):
    for i in range(withdraw):
        time.sleep(0.1)
        Bal.value=Bal.value-1

if __name__=="__main__":
    Balance=multiprocessing.Value('d',200)

    P1=multiprocessing.Process(target=deposit,args=(100,Balance))
    P2 = multiprocessing.Process(target=withdraw, args=(100, Balance))

    P1.start()
    P2.start()

    P1.join()
    P2.join()

    print("Final Balance: ",Balance.value)

