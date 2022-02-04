# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        curr = dummy
        while curr.next and curr.next.next:
            B = curr.next
            A = curr.next.next
            C = curr.next.next.next
            curr.next = A
            curr.next.next = B
            curr.next.next.next = C
            curr = curr.next.next
        return dummy.next
