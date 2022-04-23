# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        max_val = max(nums)
        max_idx = nums.index(max_val)
        left_child = self.constructMaximumBinaryTree(nums[0:max_idx]) if max_idx > 0 else None
        right_child = self.constructMaximumBinaryTree(nums[max_idx+1:]) if max_idx < len(nums) - 1 else None
        return TreeNode(max_val, left_child, right_child)
