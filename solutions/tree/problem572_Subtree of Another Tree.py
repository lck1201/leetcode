# recursively
# 看清楚题目要求，子树的定义
def isSame(s,t):
    if not s and not t:
        return True
    if not s or not t:
        return False

    if s.val != t.val:
        return False

    return isSame(s.left, t.left) and isSame(s.right, t.right)

class Solution():
    def isSubtree(self, s, t):
        if not s or not t:
            return False

        if isSame(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

# # iterative
# def inorder_travel(node):
#     re = []
#     if node:
#         re.extend(inorder_travel(node.left))
#         re.append(node.val)
#         re.extend(inorder_travel(node.right))
#
#     return re
#
# class Solution2:
#     def isSubtree(self, s, t):
#         """
#         :type s: TreeNode
#         :type t: TreeNode
#         :rtype: bool
#         """
#         if not s and not t:
#             return True
#
#         if not t:
#             return True
#
#         subtree_val = inorder_travel(t)
#
#         q = list()
#         q.append(s)
#         while len(q):
#             the_node = q.pop()
#             the_node_val = inorder_travel(the_node)
#
#             if subtree_val == the_node_val:
#                 return True
#
#             if the_node.left:
#                 q.append(the_node.left)
#             if the_node.right:
#                 q.append(the_node.right)
#
#         return False
