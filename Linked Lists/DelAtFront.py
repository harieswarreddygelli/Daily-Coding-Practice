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
        
    def delatfront(self):
        self.head=self.head.next
        return self.head
  
    def display(self):
        current = self.head
        while current:
          print(current.data,"-> ",end=" ")
          current=current.next
        print("None")

a=int(input("Enter how many items you want to insert: "))
lils=LinkedList()
print("Enter items: ")
for _ in range(a):
    li=input("")
    lils.append(li)
lils.display()
n=input("Do you want to item at front (y/n): ")
if n=="y":
    lils.delatfront()
    print("After deletion  At that front:")
    lils.display()

