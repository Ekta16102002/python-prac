print("33_ITB_Ekta singh")
class Node():
  def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class circulardoublyLinkedList():
  def __init__(self):
        self.root=self.last=None
  def insertLeft(self,data):
    n=Node(data)
    if self.root==None:#not created
            self.root=self.last=n#root created
    else:
            n.right=self.root#1
            self.root.left=n#2
            self.root=n#3
            self.last.right=self.root
            self.root.left=self.last
  def insertRight(self,data):
      n=Node(data)
      if self.root==None:#not created
        self.root=self.last=n#root created
      else:
          n.left=self.last
          self.last.right=n
          self.last=n
          self.last.right=self.root
          self.root.left=self.last
  def deleteLeft(self):
      if self.root==None:
          print("list empty")
      else:
        if self.root==None:
          print("list empty")

        else:
          t=self.root#1
          if self.last==self.root:
            self.last=self.root=None
          else: 
            self.root=self.root.right#2
            self.root.left=self.last
            self.last.right=self.root
            print("deleted",t.data)
  def deleteRight(self):
      if self.root==None:
          print("list empty")

      else:
        temp= self.last
        if self.last==self.root:
          self.last=self.root=None
        else:
          self.last=self.last.left
          self.last.right=self.root
          self.root.left=self.last
          print("deleted",temp.data)
  def printList(self):
    if self.root==None:
      print("empty list")
    else: 
          temp = self.root
          while True:
              print("<-|",temp.data,"|->",end='')
              temp = temp.right
              if temp==self.root:
                break
        

obj=circulardoublyLinkedList()
while True:
    print("\n1.insertLeft\n2.insertRight\n3.deleteLeft\n4.deleteRight\n5.print\n6.Exit")
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
        print("Exit")
        print("Developed by Ekta Singh")
        break
    else:
        print("Wrong input.")                    