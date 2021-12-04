# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        index = result
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                index.next = ListNode(l1.val)
                index = index.next
                l1 = l1.next
            else:
                index.next = ListNode(l2.val)
                index = index.next
                l2 = l2.next
        if l1 is None:
            l1, l2 = l2, l1
        while l1 is not None:
            index.next = ListNode(l1.val)
            index = index.next
            l1 = l1.next
        return result.next
