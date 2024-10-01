class customDictionary:

    def __init__(self):
        self.Max=100
        self.arr=[None for i in range(self.Max)]
    
    def getHash(self,key):
        h=0
        for i in key:
            h+=ord(i)
        
        return h % self.Max
    
    def __setitem__(self,key,item):
        ind=self.getHash(key)
        self.arr[ind]=item
        print(self.arr)
    
    def __getitem__(self,key):
        ind=self.getHash(key)
        return self.arr[ind]
    
    def __delitem__(self,key):
        ind=self.getHash(key)
        self.arr[ind]=None
        
