# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
        self.target_sum = 0

    def recursive(self, node, lst):
        if not node:
            return
        lst_new = lst + [node.val]
        if not node.left and not node.right:
            if sum(lst_new) == self.target_sum:
                self.result.append(lst_new)
                return
        self.recursive(node.left, lst_new)
        self.recursive(node.right, lst_new)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.target_sum = targetSum
        self.recursive(root, [])
        return self.result
