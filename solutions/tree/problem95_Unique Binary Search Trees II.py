# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n: int) -> 'List[TreeNode]':
        if n == 0:
            return []
        if n == 1:
            return [TreeNode(1)]
        def dfs(start, end):
            candidate = []
            if start > end:
                candidate.append(None)

            for x in range(start, end + 1):
                left_candi = dfs(start, x - 1) # here to satisfy BST rules
                right_candi = dfs(x + 1, end)
                for l in left_candi:
                    for r in right_candi:
                        root = TreeNode(x)
                        root.left = l
                        root.right = r
                        candidate.append(root)

            return candidate

        return dfs(1, n)
