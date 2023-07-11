#!/usr/bin/env python3
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#* All tests passed
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Two pointers aprach(iterative) + "tmp" so we can save next pointer
        tmp:  ListNode = None
        curr: ListNode = head
        prev: ListNode = None

        # Start loop
        while curr:
            # Save next node pointer
            tmp = curr.next
            # Point first node to prev (last node)
            curr.next = prev
            # Update "prev" to point to the new last node, "curr"
            prev = curr
            # Update "curr" to the next node to reverse
            curr = tmp
        # Return last node, curr is not last node because it is now tmp which point to None (lastNode->next)
        return prev

#* All tests passed (Iterative is better though, recursive has same time but + memory)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive solution, I don't know how to explain this without a whiteboard or 500 lines so yeah gl
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
            head.next = None
        return newHead