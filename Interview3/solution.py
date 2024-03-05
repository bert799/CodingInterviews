class Stack:
    def __init__(self):
        # Your subclass must not access this attribute
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._items)


class StackWithMin(Stack):
    # Create whatever methods you need
    def __init__(self):
        super().__init__()
        self.min_stack = Stack()
    
    def push(self, value):
        super().push(value)
        if self.min_stack.empty() or value <= self.min_stack.peek():
            self.min_stack.push(value)
    
    def pop(self):
        value = super().pop()
        if value == self.min_stack.peek():
            self.min_stack.pop()
        return value

    def minimum(self):
        # You must implement at least this method
        # AND it must be O(1) time
        return self.min_stack.peek()