inpArr=[38,2,34,8,23,4,67,6,88,9]
inpLength=len(inpArr)-1

for tempLen in range(inpLength,0,-1):
    for j in range(tempLen):
        if inpArr[j+1]<inpArr[j]:
            temp=inpArr[j+1]
            inpArr[j+1]=inpArr[j]
            inpArr[j]=temp
    print(f"Step {inpLength-tempLen+1}:{inpArr} ")
