#!/usr/bin/env python3
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Start misc functions
def createLinkedList(values):
    head: Optional[ListNode] = None
    current: Optional[ListNode] = None

    for val in values:
        node = ListNode(val)
        if head is None:
            head = node
            current = head
        else:
            current.next = node
            current = current.next
    return head

def printLinkedList(head: Optional[ListNode]) -> None:
    current: Optional[ListNode] = head

    print("Linked List:")
    while current:
        print(current.val)
        current = current.next
# End misc functions

#* Passes all tests
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #* We create a new list with a dummy first node
        dummy: Optional[ListNode] = ListNode(-1)
        dummyHead: Optional[ListNode] = dummy

        while list1 and list2:
            #* If the value of the list1 node is smaller we put that node
            if list1.val < list2.val:
                dummy.next = list1
                dummy = list1
                list1 = list1.next
            #* else we put the list2 node (because it's smaller)
            else:
                dummy.next = list2
                dummy = list2
                list2 = list2.next
        #* At the exit of the loop, its possible that not both lists have been finished, thats why here we add the remaining list to the end
        #* We can do that because we already know that it's sorted and it's the only thing missing
        if list1 or list2:
            dummy.next = list1 if list1 else list2
        #* We return "dummyHead.next" because "dummyHead" is the first node initilized to create the linked list (val = -1)
        return dummyHead.next

values = [1,2,4]
values2 = [1,3,4]
result = Solution.mergeTwoLists(Solution, createLinkedList(values), createLinkedList(values2))
printLinkedList(result)
