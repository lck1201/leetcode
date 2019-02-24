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
        self.t = None

    def push(self, x: int) -> None:
        if self.t:
            temp = Node(x)
            # p = self.t
            temp.next = self.t
            self.t = temp
            if self.minVal[-1] >= x:
                self.minVal.append(x)
        else:
            self.t = Node(x)
            self.minVal.append(x)

    def pop(self) -> None:
        if self.t:
            if self.t.val == self.minVal[-1]:
                self.minVal.pop(-1)
            next = self.t.next
            self.t = next

    def top(self) -> int:
        if self.t:
            return self.t.val

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