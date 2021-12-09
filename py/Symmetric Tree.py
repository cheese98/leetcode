# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkSymmetric(self, lefts, rights):
        if not lefts and not rights:
            return True
        if not lefts or not rights:
            return False
        if lefts.val != rights.val:
            return False
        outer = self.checkSymmetric(lefts.left, rights.right)
        inner = self.checkSymmetric(lefts.right, rights.left)
        return outer and inner

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.checkSymmetric(root.left, root.right)
