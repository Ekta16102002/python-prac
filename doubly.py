print("33_ITB_Ekta singh")
class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

class DoublyLinkedList:
    def __init__(self):
      self.root=None        

    def insertLeft(self,data):
        n=Node(data)
        if self.root==None:#not created
            self.root=n#root created
        else:
            n.right=self.root#1
            self.root.left=n#2
            self.root=n#3

    def deleteLeft(self):
        if self.root==None:
            print("Empty List")
        else:
            t=self.root#1
            self.root=self.root.right#2
            self.root.left=None#3
            print("Deleted:",t.data)  

    def insertRight(self,data):
        n=Node(data)
        if self.root==None:
           self.root=n
        else:
            t=self.root#1
            while t.right!=None:#2
                t=t.right
            t.right=n#3
            n.left=t#4


    def deleteRight(self):
        if self.root==None:
            print("Empty List")
        else:
            t=self.root#1
            while t.right!=None:#2
                t=t.right
            if t==self.root:
                self.root=None
            else:
                t2=t.left#3
                t2.right=None#4

            print("Deleted:",t.data)
    

    def printList(self):
        if self.root==None:
            print("Empty List")
        else:
            temp = self.root
            while temp !=None:
                print("|",temp.data,"|->",end='')
                temp = temp.right
    def printListRev(self):
        if self.root==None:
            print("Empty List")
        else:
            temp = self.root#1
            while temp.right!=None:#2
                temp = temp.right 
            while temp!=None:#3
                print("|",temp.data,"|->",end='')
                temp=temp.left


obj=DoublyLinkedList()
while True:
    print("\n1.insertLeft\n2.insertRight\n3.deleteLeft\n4.deleteRight\n5.print\n6.print Reverse\n7.Exit")
    ch=int(input("Enter:"))
    if ch==1:
      data=int(input("Enter data:"))
      obj.insertLeft(data)
      print("Element added",data)

    elif ch==2:            
      data=int(input("Enter data:"))
      obj.insertRight(data)
      print("Element added",data)

    elif ch==3:
      obj.deleteLeft()

    elif ch==4:
      obj.deleteRight()

    elif ch==5:
      obj.printList()

    elif ch==6:
      obj.printListRev()

    elif ch==7:
        print("Exit")
        print("Developed by Ekta Singh")
        break
    else:
        print("Wrong input.")                    