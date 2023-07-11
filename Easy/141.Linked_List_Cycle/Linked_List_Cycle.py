#!/usr/bin/env python3
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#* All tests passed
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # We create a list to store the nodes
        nodeList: List[ListNode] = []

        # We iterate through the list
        while head:
            # If we are visiting a node already on "nodeList", return True (linked list with a cycle)
            if head in nodeList:
                return True
            # We add every new node to the list so we can check it after in the if above
            nodeList.append(head)
            head = head.next
        # If there is a final null (linked list without a cycle), we will exit the loop and return False
        return False


#* All tests passed (Floyd's Tortoise and Hare algo)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Definition of two pointers for algo
        bicycle: ListNode = head
        bugatti: ListNode = head

        # Imagine you have 2 cars running on a circle, if one car is twice as fast, there is going to be a moment were
        # that fast car caches up again with the slow car, thats the idea of this algo. I've named the variables as vehicles for easier understanding
        while bugatti and bugatti.next:
            bicycle = bicycle.next
            bugatti = bugatti.next.next
            # Check if they are at the same position (same node)
            if bicycle == bugatti:
                return True
        return False