integer1 = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]

res1={x:y for x,y in zip(integer1,binary)}

print("Result 1 : ",res1)


#additive inverse

integer2=[-2,-1,0,1,2]

res2=[0-x for x in integer2]

print(f'result 2 : {res2}')

#unique squares
integer3 = [1, -1, 2, -2, 3, -3]

set={i*i for i in integer3}

print("Result3 :",set)

