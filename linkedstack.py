print("33_ITB_Ekta singh")
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class DynamicStack:
    def __init__(self):
        self.tos=None
    def push(self,data):
        n=Node(data)
        if self.tos==None:#not created
            self.tos=n#root created
        else:
            n.next=self.tos
            self.tos=n
    def pop(self):
        if self.tos==None:
            print("Empty Stack")
        else:
            t=self.tos#1
            self.tos=self.tos.next#2
            print(t.data)
            #del t
    def peek(self):
        if self.tos==None:
            print("Stack Empty")
        else:
            print(self.tos.data)
    def printStack(self):
        if self.tos==None:
            print("Stack Empty")
        else:
            temp = self.tos
            while temp!=None:
                print("|",temp.data,"|->",end='')
                temp = temp.next


o=DynamicStack()
while True:
    print("\n1.Push\n2.Pop\n3.Peek\n4.Print\n5.Exit")
    ch=int(input("Enter:"))
    if ch==1:
            data=int(input("Enter data:"))
            o.push(data)
            print("Element pushed")
    elif ch==2:
            print("Element poped:",o.pop())

    elif ch==3:
            o.peek()

    elif ch==4:
            print("Elements is stack")
            o.printStack()

        
    elif ch==5:
        print("Exit")
        break
    else:
        print("Wrong input")