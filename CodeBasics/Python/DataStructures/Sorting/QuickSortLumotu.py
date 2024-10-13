def quickSort(l,p,pivot):

    leftList,rightList,cnt,i=[],[],pivot,0
    
    #if list length is less than 2 return list as such
    if pivot < 1:
        return l

    while p!=pivot and i!=pivot:
        #increment pointer p till it finds larger element than pivot
        while l[p]<l[pivot]:
            p+=1
        
        
        if p==pivot:
            break

        i=p+1
        #increment pointer i till it finds larger element than pivot
        while l[i]>l[pivot]:
            i+=1
 
        if l[i]<l[pivot]:
            l[i],l[p]=l[p],l[i]
            #print(f"Swapping i and p {l} i={i} p={p}")

    if p==pivot:
        #print(f"Left List= {l[0:pivot]}")
        leftList=quickSort(l[0:pivot],0,p-1)  

    if i==pivot:
        #print(f"swapping p and pivot p={p} pivot={pivot}")
        l[p],l[pivot]=l[pivot],l[p]
        pivot=p

        #print(f"Left List= {l[0:pivot]}")
        leftList=quickSort(l[0:pivot],0,p-1)

        #print(f"Right List= {l[pivot+1:]}")
        rightList=quickSort(l[pivot+1:],0,cnt-pivot-1)

 
   
   
    return leftList+[l[pivot]]+rightList

tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

for l in tests:
    print(quickSort(l,0,len(l)-1))





