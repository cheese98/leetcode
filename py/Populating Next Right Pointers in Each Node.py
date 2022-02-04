"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def access(self, node, idx):
        order = bin(idx)[3:]
        for x in order:
            if x == '0':
                node = node.left
            else:
                node = node.right
        return node
    
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        i = 1
        rightest = 1
        prev = root
        while True:
            next = self.access(root, i + 1)
            if not next:
                prev.next = None
                break
            if i != rightest:
                prev.next = next
            else:
                prev.next = None
                rightest = rightest * 2 + 1
            prev = next
            i += 1
        return root
