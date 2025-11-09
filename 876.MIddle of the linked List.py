import math
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        original_head = head
        while head:
            length += 1
            head = head.next
        middle = math.ceil(length / 2 +0.1)
        head = original_head
        for i in range(middle - 1):
            head = head.next
        return head


node_6 = ListNode(val=6)
node_5 = ListNode(val=5, next=node_6)
node_4 = ListNode(val=4, next=node_5)
node_3 = ListNode(val=3, next=node_4)
node_2 = ListNode(val=2, next=node_3)
node_1 = ListNode(val=1, next=node_2)

print(Solution().middleNode(node_1).val)


node_5 = ListNode(val=5)
node_4 = ListNode(val=4, next=node_5)
node_3 = ListNode(val=3, next=node_4)
node_2 = ListNode(val=2, next=node_3)
node_1 = ListNode(val=1, next=node_2)

print(Solution().middleNode(node_1).val)
