class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 


class LinkedList:
    def __init__(self):
        self.head = None  

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def insert_at_Pos(self,pos,data):
        new_node = Node(data)
        temp=self.head
        for i in range(1,pos):
            temp=temp.next
        new_node.next,temp.next=temp.next,new_node
        
    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node     
        
    def addatend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
        
    def delatfront(self):
        self.head=self.head.next
        if self.head==None:
            return None
        return self.head
        
    def delatspepos(self,pos):
        if self.head==None:
            return None
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        temp.next=temp.next.next
        return self.head  
        
        
    def delatend(self):
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None
        return self.head
    
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,"->",end=" ")
            temp=temp.next
        print("None")

def anymod():
    print("="*30)
    print("Choose option:")
    print("1.Insertion at Front.")
    print("2.Insertion at End.")
    print("3.Insertion at a particular position.")
    print("4.Deletion at Front.")
    print("5.Deletion at End.")
    print("6.Deletion at a particular position.")
    print("7.Display The list.")
    print("8.Exit.")
    print("="*30)
    d=int(input("Enter option."))
    if d==1:
        k=input("Enter data You Want to add at front: ")
        lils.insert_at_front(k)
        print("The List after Modification.")
        lils.display()
        a=input("Do you want to make any more operations: (y/n)")
        if a=='y':
            anymod()
        
        
    elif d==2:
        k=input("Enter data You Want to add at End: ")
        lils.addatend(k)
        print("The List after Modification.")
        lils.display()
        a=input("Do you want to make any more operations: (y/n)")
        if a=='y':
            anymod()
        
        
    elif d==3:
        k=input("Enter data You Want to add at a particular position: ")
        n=int(input("Enter the position: "))
        lils.insert_at_Pos(n,k)
        print("The List after Modification.")
        lils.display()
        a=input("Do you want to make any more operations: (y/n)")
        if a=='y':
            anymod()
        
        
    elif d==4:
        lils.delatfront()
        print("The List after Deletion At Front.")
        lils.display()
        a=input("Do you want to make any more operations: (y/n)")
        if a=='y':
            anymod()
        
        
    elif d==5:
        lils.delatend()
        print("The List after Deletion at End.")
        lils.display()
        a=input("Do you want to make any more operations: (y/n)")
        if a=='y':
            anymod()
            
            
    elif d==6:
        k=int(input("Enter The position you want to delete: "))
        lils.delatspepos(k)
        print("The List after Modification.")
        lils.display()
        a=input("Do you want to make any more operations: (y/n)")
        if a=='y':
            anymod()
            
            
    elif d==7:
        print("The List :")
        lils.display()
        a=input("Do you want to make any more operations: (y/n)")
        if a=='y':
            anymod()
            
            
    elif d==8:
        print("="*10,"Thanks for Using","="*10)
        
        
    else:
        print("Enter a Correct Option:")
        anymod()
        
        
        

a=int(input("Enter size of  data  you want to insert: "))
lils=LinkedList()
print("Enter data: ")
for _ in range(a):
    li=input("")
    lils.append(li)
print("The Entered Data: ")
lils.display()
a=input("Do you want to make any more operations: (y/n)")
if a=='y':
    anymod()
    
