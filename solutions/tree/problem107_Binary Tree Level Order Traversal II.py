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


class Solution2:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
            return ans

        NodeList = [root]
        while NodeList:
            CurLevelAns = list()

            n = len(NodeList)
            for _ in range(n):
                nd = NodeList.pop(0)

                CurLevelAns.append(nd.val)
                if nd.left:
                    NodeList.append(nd.left)
                if nd.right:
                    NodeList.append(nd.right)

            ans.append(CurLevelAns)

        return list(reversed(ans))