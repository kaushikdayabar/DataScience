class customDictionary:

    def __init__(self):
        self.Max=10
        self.arr=[[] for i in range(self.Max)]
    
    def getHash(self,key):
        h=0
        for i in key:
            h+=ord(i)
        
        return h % self.Max
    
    def __setitem__(self,key,item):
        ind=self.getHash(key)
        varEnum=list(enumerate(self.arr[ind]))

        for idx,element in varEnum:
            if element[0]==key:
                self.arr[ind][idx]=(key,item)
                return
        
        self.arr[ind].append((key,item))

        print(self.arr)
    
    def __getitem__(self,key):
        ind=self.getHash(key)
        varEnum=list(enumerate(self.arr[ind]))

        for idx,element in varEnum:
            if element[0]==key:
                return element[1]

        return "Element Not found"
    
    def __delitem__(self,key):
        ind=self.getHash(key)
        varEnum=list(enumerate(self.arr[ind]))

        for idx,element in varEnum:
            if element[0]==key:
                self.arr[ind].pop(idx)
        
    
        
