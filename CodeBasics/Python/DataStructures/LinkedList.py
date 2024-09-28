class Node:

    def __init__(self,data,Next=None):
        self.Value=data
        self.Next=Next


class LinkedList:

    def __init__(self):
        self.head=None

    def insertAtBeginning(self,data):
        n=Node(data,self.head)
        self.head=n

    def insertAtEnd(self,data):
        if self.head is None:
            self.head=Node(data,None)
        else:
            itr=self.head

            while itr.Next:
                itr=itr.Next

            itr.Next=Node(data,None)

    #to create a fresh Linked List based on a set of values 
    def insertValues(self,dataList:list):

        self.head=None

        for i in dataList:
            self.insertAtEnd(i)

    def getLength(self):
        itr=self.head
        cnt=0

        while itr:
            cnt+=1
            itr=itr.Next

        return cnt

    # To remove item from specific index

    def removeIndex(self,indexVal):
        if indexVal<0 or self.getLength()<=indexVal:
            raise Exception("Invalid Index")
        else:
            if indexVal==0:
                self.head=self.head.Next
            else:
                cnt=indexVal-1
                itr=self.head
                while cnt!=0:
                    cnt-=1
                    itr=itr.Next
                itr.Next=itr.Next.Next

    #insert at specified index

    def insertAt(self,indexVal,data):
        print(f"index={indexVal} Data={data}")

        if indexVal<0 or indexVal>self.getLength():
            raise Exception("Invalid Index")
        else:
            if indexVal==0:
                n=Node(data,self.head)
                self.head=n
            else:
                itr=self.head
                cnt=indexVal-1
                while cnt!=0:
                    cnt-=1
                    itr=itr.Next
                n=Node(data,itr.Next)
                itr.Next=n

    #insert after a value
    def insertAfter(self,dataAfter,data):

        itr=self.head

        if itr==None:
            return
        else:
            while itr.Value!=dataAfter and itr.Next!=None:
                print(itr.Value)
                itr=itr.Next

        if itr.Value==dataAfter:
            n=Node(data,itr.Next)
            itr.Next=n    
        
    def removeValue(self,data):
        itr=self.head
        
        if itr is None:
            return
        elif itr.Value==data:
            self.head=self.head.Next
        elif itr.Next!=None:
            while itr.Next.Value!=data and itr.Next.Next!=None:
                itr=itr.Next
        

        if itr.Next!=None:
            if itr.Next.Value==data:
                itr.Next=itr.Next.Next
      
            
        
                    

    def printList(self):

        if self.head==None:
            print("Linked List is empty")
        else:
            itr=self.head
            LinkedListRes=''
            while itr.Next!=None:
                LinkedListRes+=str(itr.Value)+"-->"
                itr=itr.Next
            LinkedListRes+=str(itr.Value)
            print(LinkedListRes)


if __name__=="__main__":
    LL1=LinkedList()

    print("1.Insert At Beginning\n2.Insert At End\n3.To Create Fresh Linked List\n4.Get Length \n5. To Remove Item from specified Index"
              "\n6.To Insert at Speficied Index \n7.To Insert after a value\n8.To Remove a Value")

    op=0

    while op==0:
        LL1.printList()
        

        OpS=int(input("Please Enter your Operation"))

        if OpS==1:
            varData=input("Please enter Value")
            LL1.insertAtBeginning(varData)
        elif OpS==2:
            varData=input("Please enter Value")
            LL1.insertAtEnd(varData)
        elif OpS==3:
            varDataArr=input("Please Enter Array").split(" ")
            LL1.insertValues(varDataArr)
        elif OpS==4:
            print(LL1.getLength())
        elif OpS==5:
            varIndexVal=int(input("Please Enter Index"))
            LL1.removeIndex(varIndexVal)
        elif OpS==6:
            varIndexData=input("Please Enter Data")
            varIndexVal=int(input("Please Enter Index"))
            LL1.insertAt(varIndexVal,varIndexData)
        elif OpS==7:
            varIndexData=input("Please Enter Data")
            varPrevVal=input("Please Enter Previous Value")
            LL1.insertAfter(varPrevVal,varIndexData)
        elif OpS==8:
            varData=input("Please Enter Data")
            LL1.removeValue(varData)
        else:
            print("Please enter values from 1 to 7")
        LL1.printList()
        op=int(input("Do you want to continue operation?"))

        
        
            
