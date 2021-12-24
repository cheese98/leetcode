# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        A = head
        B = head
        while B and B.next:
            A = A.next
            B = B.next.next
            if A is B:
                return True
        return False
