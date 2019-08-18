# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import collections


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        vals = []

        def preOrder(node):
            if node:
                vals.append(node.val)
                preOrder(node.left)
                preOrder(node.right)

        preOrder(root)
        return ' '.join(map(str, vals))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = collections.deque(int(val) for val in data.split())

        def decode(minVal, maxVal):
            if vals and minVal < vals[0] < maxVal:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = decode(minVal, val)
                node.right = decode(val, maxVal)

                return node

        return decode(float('-inf'), float('inf'))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
