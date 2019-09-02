# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def dfs(self, node):
        if not node:
            return 0

        leftDepth = self.dfs(node.left)
        rightDepth = self.dfs(node.right)

        # to get max diameter
        self.ans = max(leftDepth + rightDepth + 1, self.ans)

        return max(leftDepth, rightDepth) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> 'int':
        if not root:
            return 0

        self.ans = 0
        self.dfs(root)
        return self.ans - 1

class Solution2:
    def printLongestLeafLeafPath(self, root: TreeNode):
        if not root:
            return 0

        ans = []
        def dfs(node):
            nonlocal ans
            if not node:
                return list()

            leftLongestPath = dfs(node.left)
            rightLongestPath = dfs(node.right)

            tmpAns = leftLongestPath + [node.val] + rightLongestPath
            if len(tmpAns) > len(ans):
                ans = tmpAns
            return [node.val] + (leftLongestPath if len(leftLongestPath) > len(rightLongestPath) else rightLongestPath)

        dfs(root)
        return ans