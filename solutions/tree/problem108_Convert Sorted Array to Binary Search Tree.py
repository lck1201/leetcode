# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: 'List[int]') -> 'TreeNode':
        if len(nums) == 0:
            return None

        midIndex = len(nums)//2
        root = TreeNode(nums[midIndex])

        root.left = self.sortedArrayToBST(nums[:midIndex])
        root.right = self.sortedArrayToBST(nums[midIndex+1:])

        return root