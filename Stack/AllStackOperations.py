class Stack:
  def __init__(self):
    self.items=[]
    
    
  def push(self,data):
    self.items.append(data)
    
    
  def pop(self):
    if len(self.items)==0:
      return "Stack Underflow"
    else:
      print("The Element Deleted is :",self.items.pop())
      
      
  def display(self):
     print(self.items)
    
    
  def peek(self):
    if  self.items:
         print(self.items[-1])
    else:
        print("Stack Underflow.")
    
    
def anymod():
    print("="*30)
    print("Choose option:")
    print("1.Insertion.")
    print("2.Deletion")
    print("3.Display The Stack.")
    print("4.Peek Element.")
    print("5.Exit.")
    print("="*30)
    d=int(input("Enter option."))
    if d==1:
        k=input("Enter data You Want to add : ")
        st.push(k)
        print("The stack after Modification.")
        st.display()
        a=input("Do you want to make any more operations: (y/n)")
        if a=='y':
            anymod()
    
    
    elif d==2:
        st.pop()
        print("The Stack after Deletion .")
        st.display()
        a=input("Do you want to make any more operations: (y/n)")
        if a=='y':
            anymod()
            
            
    elif d==3:
        print("The Stack :")
        st.display()
        a=input("Do you want to make any more operations: (y/n)")
        if a=='y':
            anymod()
            
            
    elif d==4:
        print("The peek Element in the Stack is  :")
        st.peek()
        a=input("Do you want to make any more operations: (y/n)")
        if a=='y':
            anymod()
            
            
    elif d==5:
        print("="*10,"Thanks for Using","="*10)
        
    else:
        print("Enter a Correct Option:")
        anymod()
        
if __name__ == "__main__":
    st=Stack()
    a=int(input("Enter how many elements you want to add in the stack:  "))
    for i in range(a):
        k=input("Enter Elements: ")
        st.push(k)
    print("The Stack now:")
    st.display()
    d=input("Do you want any modifications:(y/n)")
    if d=='y':
        anymod()
