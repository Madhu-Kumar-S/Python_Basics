import array as arr


class Stack:
    def __init__(self):
        self.top = -1
        self.size = int(input("Enter the size of array:"))
        self.a = arr.array('i', [])

    def is_empty(self):
        if self.top == -1:
            print("Stack is Empty")
        else:
            print("stack is not empty")

    def is_full(self):
        if self.top == self.size - 1:
            print("Stack is full")
        else:
            print("Stack is not Full")

    def push(self, val):
        self.top = self.top + 1
        self.a.append(val)

    def pop(self):
        self.a[self.top] = 0
        self.top -= 1

    def display(self):
        print(*self.a)

    def length(self):
        count = 0
        for i in self.a:
            count += 1
        print("Length of stack is: ", count)


stack = Stack()
while True:
    print("1 for push")
    print("2 for pop")
    print("3 to check if empty")
    print("4 to check if full")
    print("5 for display")
    print("6 for getting length")
    print("0 for exit")
    option = int(input("enter ur option:"))
    if option == 1:
        value = int(input("Enter an element:"))
        stack.push(value)
    elif option == 2:
        stack.pop()
    elif option == 3:
        stack.is_empty()
    elif option == 4:
        stack.is_full()
    elif option == 5:
        stack.display()
    elif option == 6:
        stack.length()
    else:
        break
