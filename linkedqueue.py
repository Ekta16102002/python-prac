print("33_ITB_Ekta singh")
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class DynamicQueue:
    def __init__(self):
        self.front=self.rear=None
    
    def Dequeue(self):
        if self.front==None:
            print("Empty Queue")
        else:
            t=self.front#1
            self.front=self.front.next#2
            print("Deleted:",t.data)
         
    def Enqueue(self,data):
        n=Node(data)
        if self.front==None:
            self.front=self.rear=n
        else:
            self.rear.next=n
            self.rear=n
        
    def printQueue(self):
        temp = self.front
        while temp!=None:
            print("|",temp.data,"|->",end='')
            temp = temp.next


obj=DynamicQueue()
while True:
    print("\n1.Enqueue\n2.Dequeue\n3.Print\n4.Exit")
    ch=int(input("Enter:"))
    if ch==1:
            data=int(input("Enter data:"))
            obj.Enqueue(data)
            print("Element Enqueued")

    elif ch==2:
            print(obj.Dequeue())

    
    elif ch==3:
            print("Element in Queue:")
            obj.printQueue()

    elif ch==4:
        print("Exit:")
        print("Developed by Ekta Singh")
        break
    else:
        print("Wrong input.")    