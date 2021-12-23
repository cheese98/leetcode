# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def extractList(node, arr):
            if node:
                arr.append(node)
                extractList(node.next, arr)
        listA = []
        listB = []
        extractList(headA, listA)
        extractList(headB, listB)
        if listA[-1] != listB[-1]:
            return None
        cap = min(len(listA), len(listB))
        for i in range(1, cap + 1):
            if listA[-i] != listB[-i]:
                return listA[-i + 1]
        return listA[-cap]
