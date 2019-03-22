# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> 'List[List[int]]':
        if not root:
            return []

        ans = [[]]
        curDepth = 0
        queue = [root]
        while queue:
            if len(ans) < curDepth + 1:
                ans.append([])

            n = len(queue)
            for idx in range(n):
                node = queue.pop(0)

                ans[curDepth].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            curDepth += 1

        return list(reversed(ans))