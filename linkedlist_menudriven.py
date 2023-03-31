print("33_ITB_Ekta Singh")
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.root=None
    def insertLeft(self,data):
        n=Node(data)
        if self.root==None:#not created
            self.root=n#root created
        else:
            n.next=self.root
            self.root=n
    def deleteLeft(self):
        if self.root==None:
            print("Empty List")
        else:
            t=self.root#1
            self.root=self.root.next#2
            print("Deleted:",t.data)
            #del t
    def insertRight(self,data):
        n=Node(data)
        if self.root==None:
            self.root=n
        else:
            t=self.root#1
            while t.next!=None:#2
                t=t.next
            t.next=n#3
    def deleteRight(self):
        if self.root==None:
            print("Empty List")
        else:
            t=t2=self.root#1
            while t.next!=None:#2
                t2=t
                t=t.next
            t2.next=None#3
            if t==self.root:#manually deleting root
                self.root=None
            print("Deleted:",t.data)
            #del t
    def printList(self):
        temp = self.root
        if self.root==None:
            print("Empty List")
        else:
            while temp!=None:
                  print("|",temp.data,"|->",end='')
                  temp = temp.next
    def search(self,key):
        if self.root==None:
            print("Empty List")
        else:
            temp = self.root
            while temp!=None:
                if temp.data==key:
                    return True
                temp = temp.next
            return False
    def deleteKey(self,key):
        if self.root==None:
            print("Empty List")
        else:
            t = t2= self.root
            while t!=None and t.data!=key:
                t2=t
                t=t.next
            if t!=None:#Found
                if t==self.root:#case1
                    self.root=self.root.next
                elif t.next==None:
                    t2.next=None#t.nexts
                else:
                    t2.next=t.next
                print("Deleted:",t.data)
            else:
                print(key,"Not Found in List")
    def searchCount(self,key):
        count=-1
        if self.root==None:
            print("Empty List")
        else:
            temp = self.root
            while temp!=None:
                count+=1
                if temp.data==key:
                    return count
                temp = temp.next
            return -1


obj=LinkedList()
while True:
    print("\n1.InsertLeft\n2.DeleteLeft\n3.InsertRight\n4.DeleteRight\n5.Print\n6.Search\n7.DeleteKey\n0.Exit")
    ch=int(input("Enter:"))
    if ch==1:
        data=int(input("Enter Data:"))
        obj.insertLeft(data)
    elif ch==2:
        obj.deleteLeft()
    elif ch==3:
        data=int(input("Enter Data:"))
        obj.insertRight(data)
    elif ch==4:
        obj.deleteRight()
    elif ch==5:
        obj.printList()
    elif ch==6:
        data=int(input("Enter Key:"))
        if obj.searchCount(data)!=-1:
            print("Key found at ",obj.searchCount(data))
    elif ch==7:
        data=int(input("Enter Data for deleting:"))
        obj.deleteKey(data)
    elif ch==0:
        print("Developed by Ekta.")
        break
    else:
        print("Wrong input.")            