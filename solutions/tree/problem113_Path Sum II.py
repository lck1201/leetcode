# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> 'List[List[int]]':
        ans = []
        if not root:
            return ans

        def dfs(node, target, path):
            if not node:
                return

            if target-node.val==0 and not node.left and not node.right:
                ans.append(path + [node.val])
                return

            if node.left:
                dfs(node.left, target - node.val, path + [node.val])
            if node.right:
                dfs(node.right, target - node.val, path + [node.val])

        dfs(root, sum, [])
        return ans
