# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traversalHelper(node):
            if not node:
                return
            if node.left:
                traversalHelper(node.left)
            log.append(node.val)
            if node.right:
                traversalHelper(node.right)
        log = []
        traversalHelper(root)
        return log
