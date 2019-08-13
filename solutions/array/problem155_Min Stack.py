class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minVal = list()
        self.top = None

    def push(self, x: int) -> None:
        newNode = Node(x)
        newNode.next = self.top
        self.top = newNode

        if not self.minVal or x <= self.minVal[-1]:
            self.minVal.append(x)
        else:
            self.minVal.append(self.minVal[-1])

    def pop(self) -> None:
        if self.top and self.minVal:
            self.minVal.pop(-1)
            next = self.top.next
            self.top = next

    def top(self) -> int:
        if self.top:
            return self.top.val

    def getMin(self) -> int:
        if self.minVal:
            return self.minVal[-1]

# Your MinStack object will be instantiated and called as such:
# minStack = MinStack()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
# print(minStack.getMin())
# minStack.pop()
# print(minStack.top())
# print(minStack.getMin())