# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        node_size = 1
        tail = head
        while tail.next:
            node_size += 1
            tail = tail.next
        tail.next = head
        k %= node_size
        cursor = head
        for _ in range(node_size - k - 1):
            cursor = cursor.next
        ans, cursor.next = cursor.next, None
        return ans
