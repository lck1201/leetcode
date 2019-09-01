# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# best, to review
class Solution2:
    def pathSum(self, root: 'TreeNode', target: 'int') -> 'int':
        self.result = 0
        self.helper(root, target, 0, {0: 1})
        return self.result

    def helper(self, node, target, so_far, cache):
        # so_far is to record the sum from root to this node's parent
        # cache is to save all sums (root->predecessor) of all of this node's predecessors
        if node:
            complementary = so_far + node.val - target # sum(root->node) - target is what we need in the previous path
            if complementary in cache:
                self.result += cache[complementary]

            cache[so_far + node.val] = cache.get(so_far + node.val, 0) + 1
            self.helper(node.left, target, so_far + node.val, cache)
            self.helper(node.right, target, so_far + node.val, cache)
            cache[so_far + node.val] -= 1
        return


# brute-force
# class Solution:
#     def dfs(self, node, target):
#         if not node:
#             return
#
#         if target - node.val == 0:
#             self.result += 1
#
#         self.dfs(node.left, target - node.val)
#         self.dfs(node.right, target - node.val)
#
#     def pathSum(self, root: TreeNode, sum: int) -> int:
#         if not root:
#             return 0
#
#         self.result = 0
#         start = [root]
#         while start:
#             node = start.pop(0)
#             self.dfs(node, sum)
#             if node.left:
#                 start.append(node.left)
#             if node.right:
#                 start.append(node.right)
#
#         return self.result

