# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
            return ans

        NodeList = list()
        NodeList.append(root)
        while NodeList:
            tmp = list()

            n = len(NodeList)
            for _ in range(n):
                nd = NodeList.pop(0)

                tmp.append(nd.val)
                if nd.left:
                    NodeList.append(nd.left)
                if nd.right:
                    NodeList.append(nd.right)

            ans.append(tmp)

        return ans