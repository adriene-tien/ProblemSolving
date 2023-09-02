class MinStack:

    # all methods O(1), space O(n) with min elem stack and stack
    def __init__(self):
        self.stack = []
        self.min_elem_stack = []

    # O(1) time
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_elem_stack) == 0 or val <= self.min_elem_stack[-1]:
            self.min_elem_stack.append(val)
        
    # O(1) time
    def pop(self) -> None:
        if self.stack[-1] == self.min_elem_stack[-1]: 
            self.min_elem_stack.pop()
        self.stack.pop()

    # O(1) time
    def top(self) -> int:
        return self.stack[-1]
        
    # O(1) time
    def getMin(self) -> int:
        return self.min_elem_stack[-1]