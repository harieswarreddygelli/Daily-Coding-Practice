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
  def Display(self):
    return self.items
    
  def peek(self):
    if  self.items:
        return self.items[-1]
    raise IndexError("peek from empty stack")
    
if __name__ == "__main__":
    st=Stack()
    a=int(input("Enter how many elements you want to add in the stack:  "))
    for i in range(a):
        k=input("Enter Elements: ")
        st.push(k)
    print("The peek Element in the Stack is ",st.peek())
