# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def helper(root):
            if root:
                vals.append(str(root.val))
                helper(root.left)
                helper(root.right)
            else:
                vals.append('#')

        vals = []
        helper(root)

        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        # :type data: str
        :rtype: TreeNode
        """
        def helper():
            val = vals.pop(0)
            if val == '#':
                return None
            nd = TreeNode(int(val))
            nd.left = helper()
            nd.right = helper()
            return nd

        vals = data.split()

        return helper()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))