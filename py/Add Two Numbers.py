# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode()
        pt = ans
    
        while True:
            
            if l1:
                first = l1.val
                l1 = l1.next
            else:
                first = 0
            if l2:
                second = l2.val
                l2 = l2.next
            else:
                second = 0
            sum = first + second + pt.val
            pt.val = sum % 10
            pt.next = ListNode(sum // 10)
    
            if l1 is None and l2 is None:
                if pt.next.val == 0:
                    pt.next = None
                break
            
            pt = pt.next
    
        return ans
