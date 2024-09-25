dict1={"info":[600,630,620],"ril":[1430,1490,1567],"mtl":[234,180,160]}

def PrintStock():
    for i,l in dict1.items():
        print(f"{i}==>{l}==>avg:{sum(l)/len(l)}")


def addStock():
    stockName=input("please enter stock ")
    price=int(input("please enter price "))
    if stockName in dict1:
        dict1[stockName].append(price)
    else:
        dict1[stockName]=[price]


if __name__=="__main__":
    
    endOp=0
    while endOp!=1:
        operation=input("please provide your operation ")
        if operation=="add":
            addStock()
            PrintStock()
        elif operation=="print":
            PrintStock()
        else:
            print("Invalid Operation")
        
        endOp=int(input("If you want to execute more operations, enter 0 else 1 "))
        


    
