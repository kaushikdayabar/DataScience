import math 

def circle_calc(radious=5):
    l=[]
    l.append(math.pi*math.pow(radious,2))
    l.append(2*math.pi*radious)
    l.append(2*radious)
    return l


if __name__=="__main__":
    rad=int(input("please enter radious "))
    r=circle_calc(rad)
    print(f"Diameter={r[2]}\nCircumference={r[1]}\nArea={r[0]}")

    
    
    
    
