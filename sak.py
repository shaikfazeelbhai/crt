stack=[]
top=-1
def push(value):
    global top
    top=-1
    if(top==4):
     return"stack is ful"
    else:
        top=top+1
        return stack.append(value)
def pop():
    global top
    if (top!=-1):
     return stack.pop()
    else:
      top=-1
      return"stack isempty" 
def peek():
    if (top==-1): 
        return "stack is empty"
    else:
        return f"top element={stack[top]}"
def display():
    if (top==-1):
        print("empty")
    else:
        for i in range(top,-1,-1):
            print(stack[i])
    stack=[10]
    push(10)
    push(90)
    push(30)
    push(40)
    pop()
    pop()
    print(peek())
    print(pop())
    print(stack)
    display()

    
