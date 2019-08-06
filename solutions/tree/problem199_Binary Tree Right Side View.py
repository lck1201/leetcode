# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return list()
        if not root.left and not root.right:
            return [root.val]

        ans = []
        nodeQueue = [root]
        while nodeQueue:
            ans.append(nodeQueue[0].val)

            currentLevelNodeNum = len(nodeQueue)
            for _ in range(currentLevelNodeNum):
                nd = nodeQueue.pop(0)
                if nd.right:
                    nodeQueue.append(nd.right)
                if nd.left:
                    nodeQueue.append(nd.left)
        return ans
