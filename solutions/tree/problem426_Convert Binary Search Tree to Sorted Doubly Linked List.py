class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# build Binary Search Tree
def buildBST(nums):
    root = None
    for x in nums:
        root = insert(root, x)
    return root


def insert(root, x):
    if not root:
        return Node(x)

    if x < root.val:
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)
    return root


# print doulble-linked-list
def print_list(head):
    p = head
    while p:
        print(p.val, end=' ')
        nxt = p.right
        if nxt:
            assert nxt.left == p
        p = nxt


class Solution:
    def __init__(self):
        self.pre = None
        self.head = None

    def inorder(self, root):
        if root.left:
            self.inorder(root.left)

        root.left = self.pre
        if not self.pre:
            self.head = root
        else:
            self.pre.right = root
        self.pre = root

        if root.right:
            self.inorder(root.right)


root = buildBST([6, 2, 4, 8, 5, 3, 7])
ans = Solution()
ans.inorder(root)
print(ans.head.val)

