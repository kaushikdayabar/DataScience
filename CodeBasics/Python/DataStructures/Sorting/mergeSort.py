def mergeSort(l):
    
    if len(l)<=1:
        return l
    
    mid=len(l)//2
    
    leftArr=l[:mid]
    rightArr=l[mid:]
    
    #partioning the arrays to single elements
    mergeSort(leftArr)
    mergeSort(rightArr)

    #This is the use of recursion, once partitioning is done we are merging the arrays
    join2Sort(leftArr,rightArr,l)

    return l


def join2Sort(l1,l2,res):

    i,j=0,0
    n1,n2=len(l1),len(l2) 
    n=n1+n2

    while i<n1 and j<n2:
        if l1[i]<l2[j]:
            res[i+j]=l1[i]
            i+=1
        else:
            res[i+j]=l2[j]
            j+=1
        
    while i<n1:
        res[i+j]=l1[i]
        i+=1
    
    while j<n2:
        res[i+j]=l2[j]
        j+=1
    
    
    return res

tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

for lists in tests:
    print(mergeSort(lists))
