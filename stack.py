class Stack:

    def __init__(self):
        self.stack = []
        self.max_stack = []

    def __iter__(self):
        yield from self.stack

    def __repr__(self):
        return str(self.stack)

    def push(self, data):
        self.stack.append(data)

        if self.max_stack == []:
            self.max_stack.append(data)
        else:
            data_max = self.max_stack[-1]
            if data > data_max:
                self.max_stack.append(data)
            else:
                self.max_stack.append(data_max)

    def pop(self):

        if self.is_empty():
            return None
        data = self.stack[-1]
        del self.max_stack[-1]
        del self.stack[-1]
        return f'Valor {data} eliminado del Stack'

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)

    def get_max(self):
        return self.max_stack[-1]



if __name__ == '__main__':

    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(10)
    stack.push(4)
    stack.push(30)
    stack.push(111)
    stack.push(10)
    stack.push(68)
    print(stack)
    print(stack.get_max())
    print(stack.stack_size())
    print(stack)
    print(stack.pop())
    print(stack.get_max())
    print(stack)
    print(stack.pop())
    print(stack.get_max())
    print(stack)
    print(stack.pop())
    print(stack.get_max())
    print(stack)