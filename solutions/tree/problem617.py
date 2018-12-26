# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        # method1: Recursively
        if t1 == None:
            return t2
        if t2 == None:
            return t1

        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        return t1

        # method2: iteration
        # if t1 == None:
        #     return t2
        # stack = []
        # stack.append([t1, t2])

        # while len(stack)>0:
        #     todo_node1, todo_node2 = stack.pop()
        #     if todo_node1 == None or todo_node2 == None:
        #         continue

        #     todo_node1.val += todo_node2.val
        #     if todo_node1.left == None:
        #         todo_node1.left = todo_node2.left
        #     else:
        #         stack.append([todo_node1.left, todo_node2.left])

        #     if todo_node1.right == None:
        #         todo_node1.right = todo_node2.right
        #     else:
        #         stack.append([todo_node1.right, todo_node2.right])

        # return t1