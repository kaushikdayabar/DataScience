l=[2,1,5,3,4,7,8,15,12]

def quickSort(l,start,end):
    p=start
    s,e=start+1,end
    leftList,rightList=[],[]
    #print(f"Initial List:{l} s={s} e={e} p{p}")
    if len(l)>1:
        #Movement of starting pointer and end pointer
        while s<=e:
            if l[p]>l[s]:
                s+=1
            elif l[p]<l[e]:
                e-=1
            else:
                l[s],l[e]=l[e],l[s]
        #print(f"e={e} p={p} s={s}")
        
        #swapping end pointer value and pivot pointer value
        l[e],l[p]=l[p],l[e]

        #print("Left List",l[0:e])

        #If left list does not consist of more than one element then no need to sort
        if e!=0:
            leftList=quickSort(l[0:e],0,e-1)
        
        #If right list does not consist of more than one element then no need to sort
        if e<end:
            #print("Right List",l[e+1:])
            rightList=quickSort(l[e+1:],0,end-e-1)
    #for empty list like quickSort([],0,-1)
    elif e==-1:
        return []
    
    #print(f"Final List: {leftList+[l[e]]+rightList}")
    return leftList+[l[e]]+rightList


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
