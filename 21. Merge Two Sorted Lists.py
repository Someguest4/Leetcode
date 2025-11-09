from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        tail = None
        while list1 and list2:

            if list1.val < list2.val:
                node = ListNode(val=list1.val, next=None)
                list1 = list1.next
            else:
                node = ListNode(val=list2.val, next=None)
                list2 = list2.next
            if not head:
                head = tail = node
            else:
                tail.next = node
                tail = node

        if tail:
            if list1:
                tail.next=list1
            elif list2:
                tail.next=list2
        else:
            if list1:
                head=list1
            elif list2:
                head=list2
        return head
