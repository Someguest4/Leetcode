from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_linked_list(head):
    while head:
        print(head.val)
        head = head.next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        node = None
        while head:
            node = ListNode(val=head.val, next=previous)
            previous = node
            head = head.next
        return node

print("Test 1")
node_2 = ListNode(val=2)
node_1 = ListNode(val=1, next=node_2)
print_linked_list(Solution().reverseList(head=node_1))
print("Test 2")
node_5 = ListNode(val=5, next=None)
node_4 = ListNode(val=4, next=node_5)
node_3 = ListNode(val=3, next=node_4)
node_2 = ListNode(val=2, next=node_3)
node_1 = ListNode(val=1, next=node_2)

print_linked_list(Solution().reverseList(head=node_1))