def quickSort(l):
    p,end=0,len(l)

    #if list length is less than 2 then return list as such
    if end<2:
        return l
        
    pivot=end-1
    
    leftList,rightList=[],[]

    #Moving all elements less than pivot to left
    for i in range(end):
        if l[i]<l[pivot]:
            l[i],l[p]=l[p],l[i]
            p+=1
    #print(f"list ={l} p={p}")
    l[p],l[pivot]=l[pivot],l[p]


    #print(f"Left List {l[0:p]}")
    leftList=quickSort(l[0:p])

    #print(f"Right List {l[p+1:]}")
    rightList=quickSort(l[p+1:])

    return leftList+[l[p]]+rightList

tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

for l in tests:
    print(quickSort(l))

    

