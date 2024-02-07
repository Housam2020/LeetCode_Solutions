# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        a = list1
        b = list2
        start = ListNode()
        c = start
        while a is not None and b is not None:
            if a.val < b.val:
                c.next = a
                a = a.next
            else:
                c.next = b
                b = b.next
            c = c.next
        # last node
        c.next = a if a != None else b
        return start.next
        
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        