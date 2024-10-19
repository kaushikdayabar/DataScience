def insertionSort(l):

    n=len(l)
    for i in range(n):
        j=i-1
        while j>-1:
            #print(f"i={i} j={j} l[i]={l[i]} l[j]= {l[j]}")
            if l[j+1]<l[j]:
                l[j+1],l[j]=l[j],l[j+1]
                #print(l)
            else:
                break
            j-=1
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
    print(insertionSort(l))