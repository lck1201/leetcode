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
            temp = []
            ChildNodeCache = []
            while NodeList:
                nd = NodeList.pop(0)
                temp.append(nd.val)
                if nd.left:
                    ChildNodeCache.append(nd.left)
                if nd.right:
                    ChildNodeCache.append(nd.right)
            ans.append(temp)
            NodeList.extend(ChildNodeCache)

        return ans