def squareFunc():
    i=0
    while True:
        i+=1
        yield i*i

ob=squareFunc()

for i in range(5):
    print(next(ob))
