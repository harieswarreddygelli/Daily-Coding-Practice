class Stack:
  def __init__(self):
    self.items=[]
  def push(self,item):
    self.items.append(item)
  def Display(self):
    return self.items
    
if __name__ == "__main__":
    st=Stack()
    a=int(input("Enter how many elements you want to add in the stack:  "))
    for i in range(a):
        k=input("Enter Elements: ")
        st.push(k)
    print(st.Display())
