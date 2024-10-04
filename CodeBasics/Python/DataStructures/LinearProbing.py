class customDictionary:

    def __init__(self):
        self.Max=10
        self.arr=[None for i in range(self.Max)]
    
    def getHash(self,key):
        h=0
        for i in key:
            h+=ord(i)
        
        return h % self.Max
    
    def __setitem__(self,key,item):
        ind=self.getHash(key)
        temp=ind

        if self.arr[temp]!=None:
            while self.arr[temp]!=None and self.arr[temp][0]!=key:
                temp+=1
                if temp==ind:
                    break
                else:
                    temp=temp%self.Max
        
        if self.arr[temp]==None or self.arr[temp][0]==key:
            self.arr[temp]=(key,item)
        else:
            print("Memory Full")

        print(self.arr)
    
    def __getitem__(self,key):
        ind=self.getHash(key)
        temp=ind

        if self.arr[temp]!=None:
            while self.arr[temp][0]!=key:
                temp+=1
                if temp==ind:
                    break
                else:
                    temp=temp%self.Max
                    if self.arr[temp]==None:
                        break
        
        if self.arr[temp]!=None:
            if self.arr[temp][0]==key:
                return self.arr[temp][1]
        else:
            print("Not found")
    
    def __delitem__(self,key):
        ind=self.getHash(key)
        temp=ind

        if self.arr[temp]!=None:
            while self.arr[temp][0]!=key:
                temp+=1
                if temp==ind:
                    break
                else:
                    temp=temp%self.Max
                    if self.arr[temp]==None:
                        break
        
        if self.arr[temp]!=None:
            if self.arr[temp][0]==key:
                self.arr[temp]=None
        else:
            print("Not found")
        
        print(self.arr)
        
