# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> 'List[List[int]]':
        if not root:
            return []

        ans = []
        stacks = [[], []]
        current = 0
        next = 1
        stacks[current].append(root)

        # cur_depth = 0
        while stacks[current]:
            # node = stacks[current].pop()
            #
            # while len(ans) < cur_depth + 1:
            #     ans.append([])
            #
            # ans[cur_depth].append(node.val)
            #
            # if current == 0:
            #     if node.left:
            #         stacks[next].append(node.left)
            #     if node.right:
            #         stacks[next].append(node.right)
            # else:
            #     if node.right:
            #         stacks[next].append(node.right)
            #     if node.left:
            #         stacks[next].append(node.left)
            #
            # if len(stacks[current]) == 0:
            #     cur_depth += 1
            #
            #     current = 1 - current
            #     next = 1 - next

            # NOTE: another recursive process
            tempAns = []
            for idx in range(len(stacks[current]),-1,-1):
                node = stacks[current][idx]
                tempAns.append(node.val)

                if current == 0:
                    if node.left:
                        stacks[next].append(node.left)
                    if node.right:
                        stacks[next].append(node.right)
                else:
                    if node.right:
                        stacks[next].append(node.right)
                    if node.left:
                        stacks[next].append(node.left)

            stacks[current].clear()
            current = 1 - current
            next = 1 - next
            ans.append(tempAns)

        return ans

from functools import cmp_to_key
a = {'b':1, 'b6y':166,'bg':1,'c':311,'ba':2,'be':6,'bd':10}

# a.sort(key=cmp_to_key(lambda x1,x2: x2-x1)) # list sort

import operator
a1 = sorted(a.items(), key=operator.itemgetter(1))
a2 = sorted(a.items(), key=lambda x:x[1])

print(a1,'\n', a2)