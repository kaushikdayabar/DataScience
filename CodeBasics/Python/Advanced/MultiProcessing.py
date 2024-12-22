import time
import multiprocessing

squareResult=[]
def calc_square(numbers,varMultiProcessingArray1,varValue,varQueue):
    #numbers= [2,3,8], varMultiProcessingArray1 is empty array
    global squareResult
    for n in numbers:
        #time.sleep(2)
        print('square ' + str(n*n))
        squareResult.append(n*n)
        #adding to queue
        varQueue.put(n)

    for idx,val in enumerate(numbers):
        varMultiProcessingArray1[idx]=val*val
    varValue.value=5.67
    print("Inside Process: Square Result=",squareResult)
    print("Inside Process: Multiprocessing Square Result=", varMultiProcessingArray1[:])

def calc_cube(numbers):
    for n in numbers:
        #time.sleep(2)
        print('cube ' + str(n*n*n))

if __name__ == "__main__":
    arr = [2,3,8]

    """
       declaring a multiprocessing variable so that all variables use a shared variable
       here, I have created a array variable with parameter 
       1. 'i' means integer datatype while 'd' means double
       2.size of array
       """
    varMultiProcessingArray = multiprocessing.Array('i', 3)
    """
    declaring multiprocessing variable 
    """
    varMultiValue=multiprocessing.Value('d',0.0)

    """
    Queue Variable
    
    
    """
    varQ=multiprocessing.Queue();
    print("Multiprocessing Value",varMultiValue)
    p1 = multiprocessing.Process(target=calc_square, args=(arr,varMultiProcessingArray,varMultiValue,varQ))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))


    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Outside Process : Square Result=",squareResult)
    #to display the multiprocessing array , we need to use square brackets
    print("Outside Process: Multiprocessing Square Result=", varMultiProcessingArray[:])
    #display variable value
    print(varMultiValue.value)
    print("Queue :")
    while varQ.empty() is False:
        print(varQ.get())
    print("Done!")
