def insertionSort(l,gap):
    n=len(l)
    for i in range(n):
        j=i-gap
        anchor=l[i]
        while j>-1 and anchor<l[j]:
            #print(f"i={i} j={j} l[i]={l[i]} l[j]= {l[j]}")
            l[j+gap]=l[j]
            #print(l)
            j-=gap
        l[j+gap]=anchor
        
    return l

def shellSort(l):
    #shell sort is optimization of insertion sort because if smaller elements are at last
    # then insertion sort will have to do lots of swaps hence we take some gaps and move some 
    # higher elements to last and when gap becomes one it is insertion sort and since some higher 
    # elements are atlast already, it leads to less swaps
    gap= len(l)//2

    while gap>0:
        l=insertionSort(l,gap)
        gap=gap-1
    
    return l

tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

for l in tests:
    print(shellSort(l))




    