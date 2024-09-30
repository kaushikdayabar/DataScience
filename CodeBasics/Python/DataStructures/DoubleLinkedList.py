class Node:

    def __init__(self,data,nextItem,prevItem):
        self.Data=data
        self.Prev=prevItem
        self.Next=nextItem

class DoubleLinkedList:

    def __init__(self):
        self.Head=None

    #1.Insert Data At Start
    def insertAtBeginning(self,data):
        n=Node(data,self.Head,None)

        if self.Head==None:
            self.Head=n
        else:
            self.Head.Prev=n
            self.Head=n

    #2.Insert Data at End
    def insertAtEnd(self,data):
        itr=self.Head

        if itr==None:
            self.insertAtBeginning(data)
        else:
            while itr.Next!=None:
                itr=itr.Next

            n=Node(data,None,itr)
            itr.Next=n

    #Create Fresh Linked List
    def createFreshLinkedList(self,dataArr):
        self.Head=None
        dataArr=dataArr.split(" ")

        for i in dataArr:
            self.insertAtEnd(i)

    #Get Length of Linked List
    def getLength(self):
        itr,LinkedListLength=self.Head,0

        while itr:
            itr=itr.Next
            LinkedListLength+=1

        return LinkedListLength

    #To Remove Item from specified Index
    def removeItemAtIndex(self,index):
    
        if index<0 or index>self.getLength()-1:
            print("Invalid Index")
        else:

            itr=self.Head

            for i in range(0,index):
                itr=itr.Next

            if index==0:
                self.Head=self.Head.Next
                self.Head.Prev=None
            elif index==self.getLength()-1:
                itr.Prev.Next=None
                itr.Prev=None
            else:
                itr.Prev.Next=itr.Next
                itr.Next.Prev=itr.Prev

    #Insert At Specified Index

    def insertAtSpecifiedIndex(self,varData,indexVal):

        if indexVal<0 or indexVal>self.getLength():
            print("invalid index")
        elif indexVal==0:
            self.insertAtBeginning(varData)
        else:
            itr=self.Head

            for i in range(1,indexVal):
                itr=itr.Next

            itr.Next=Node(varData,itr.Next,itr)

            if itr.Next.Next:
                itr.Next.Next.Prev=itr.Next

    #Insert After a Value
    def insertAfterValue(self,varPrevData,varData):
        itr=self.Head

        while itr:
            if itr.Data==varPrevData:
                itr.Next=Node(varData,itr.Next,itr)

                if itr.Next.Next:
                    itr.Next.Next.Prev=itr.Next
                break
            itr=itr.Next

    #Remove a Value
    def removeValue(self,data):
        itr=self.Head

        if itr.Data==data:
            self.Head=self.Head.Next
            self.Head.Prev=None
        else:
            while itr:
                if itr.Data==data:
                    itr.Prev.Next=itr.Next
                    if itr.Next:
                        itr.Next.Prev=itr.Prev
                    break
                itr=itr.Next

    
    #Print Linked in Forward
    def printLinkedListForward(self):
        itr=self.Head
        print()
        while itr:
            print(f"{itr.Data}-->",end="")
            itr=itr.Next

        print()

    #Print Linked List in Backward
    def PrintLinkedListBackward(self):
        itr=self.Head
        print()
        while itr.Next!=None:
            itr=itr.Next

        while itr:
            print(f"{itr.Data}-->",end="")
            itr=itr.Prev

        print()
        
            


if __name__=="__main__":
    DL=DoubleLinkedList()

    while 1:
        print("1.Insert At Beginning\n2.Insert At End\n3.Create Fresh Linked List",
              "\n4.Get Length of Linked List\n5.Remove Item from specified index\n6.Insert At Specified Index\n7.Insert After a Value\n8.Remove a Value\n9.Printing In Backward")
     
        Operation=int(input("Please enter your operation"))
   
        if Operation==1:
            varData=input("please enter data")
            DL.insertAtBeginning(varData)
        elif Operation==2:
            varData=input("please enter data")
            DL.insertAtEnd(varData)
        elif Operation==3:
            varData=input("please enter data Array delimited by space")
            DL.createFreshLinkedList(varData)
        elif Operation==4:
            print(DL.getLength())
        elif Operation==5:
            varIndex=int(input("Enter the Index"))
            DL.removeItemAtIndex(varIndex)
        elif Operation==6:
            varIndex=int(input("Enter the Index"))
            varData=input("Enter the Data")
            DL.insertAtSpecifiedIndex(varData,varIndex)
        elif Operation==7:
            varPrevData=input("Enter Previous Value")
            varData=input("Enter Data")
            DL.insertAfterValue(varPrevData,varData)
        elif Operation==8:
            varData=input("Enter Data")
            DL.removeValue(varData)
        elif Operation==9:
            DL.PrintLinkedListBackward()
        else:
            print("please enter valid Operation code")

        DL.printLinkedListForward()

    

        

        

    
