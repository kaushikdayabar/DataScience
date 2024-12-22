class Fibo():

    def __init__(self,limit):
        self.prev=0
        self.next=1
        self.n=0
        self.limit=limit

    def __iter__(self):
        return self

    def __next__(self):
        self.n+=1
        if self.n==self.limit:
            raise StopIteration

        else:
            if self.n==1:
                return self.prev
            elif self.n==2:
                return self.next
            else:
                result=self.prev+self.next
                self.prev=self.next
                self.next=result
                return result


ob=Fibo(7)
itr=iter(ob)

for i in range(6):
    print(next(itr))


