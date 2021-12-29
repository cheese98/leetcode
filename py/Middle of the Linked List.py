# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ln = 0
        idx = head
        while idx:
            ln += 1
            idx = idx.next
        ln //= 2
        idx = head
        for _ in range(0, ln):
            idx = idx.next
        return idx
