#!/usr/bin/env python3
from typing import *

#* All tests passed
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead: Optional[ListNode] = ListNode()
        dummy: Optional[ListNode] = dummyHead
        node: Optional[ListNode] = head

        #* Iterate through the linked list until the end or second-to-last node
        while node and node.next != None:
            #* If the current node's value is different from the next node's value
            if node.val != node.next.val:
                dummy.next = node
                dummy = dummy.next
            node = node.next
        #* Handle the last node (or the case when the list has only one node)
        if node and node.next == None:
            dummy.next = node
            dummy = dummy.next
        #* Return the first position of the sorted list
        return dummyHead.next
