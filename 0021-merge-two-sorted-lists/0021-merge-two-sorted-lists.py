# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        start = new = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                new.next = list1
                list1 = list1.next
            else:
                new.next = list2
                list2 = list2.next
            new = new.next
        # either one of list1 or list2 ran out
        while list1:
            new.next = list1
            list1 = list1.next
            new = new.next
        while list2:
            new.next = list2
            list2 = list2.next
            new = new.next
        return start.next


        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        