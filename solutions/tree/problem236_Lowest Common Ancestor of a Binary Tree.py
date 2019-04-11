# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        Heavy Solution, cost lots of time and memory
        :param root:
        :param p:
        :param q:
        :return:
        '''
        if not root:
            return None

        paths = {'p':[], 'q':[]}
        def preorder_travel(node, p, q, Path):
            if len(paths['p']) != 0 and len(paths['q']) != 0:
                return

            if node == p:
                paths['p'].extend(Path)

            if node == q:
                paths['q'].extend(Path)

            if node.left:
                preorder_travel(node.left, p, q, Path + [node.left])

            if node.right:
                preorder_travel(node.right, p, q, Path + [node.right])

        preorder_travel(root, p, q, [root])

        pPath = paths['p']
        qPath = paths['q']

        if not pPath or not qPath:
            return None

        i = 0
        while i<len(pPath) and i<len(qPath):
            if pPath[i] == qPath[i]:
                i += 1
                continue
            else:
                break

        return pPath[i-1]

# good
def lowestCommonAncestor_I(root, p, q):
    stack = [root]
    parent = {root: None}
    while p not in parent or q not in parent:
        node = stack.pop()
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)

    ancestors = set()

    while p:
        ancestors.add(p)
        p = parent[p]

    while q not in ancestors:
        q = parent[q]

    return q

# excellent
def lowestCommonAncestor_R(root, p, q):
    if root in (None, p, q):
        return root

    left = lowestCommonAncestor_R(root.left, p, q)
    right = lowestCommonAncestor_R(root.right, p, q)

    if left and right:
        return root
    else:
        return left or right