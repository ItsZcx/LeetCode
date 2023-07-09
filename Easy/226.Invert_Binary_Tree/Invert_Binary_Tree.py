#!/usr/bin/env python3
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#* All tests passed
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Create pointer to save reference to one node
        tmpNode: TreeNode = None

        # Recursively we go to the rightmost node and then swap the right and left node pointers with each other value
        if root and root.right:
            self.invertTree(root.right)
        # Same thing as avobe just for the left side
        if root and root.left:
            self.invertTree(root.left)
        # Swap the node pointers for the one next to it
        if root:
            tmpNode = root.left
            root.left = root.right
            root.right = tmpNode
        # Returns the root node
        return root

#* All tests passed
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Return None if the node is None/null
        if not root:
            return None

        # Create temp
        tmpNode: TreeNode = None

        # Swap sides
        tmpNode = root.left
        root.left = root.right
        root.right = tmpNode

        # Go to the childrens
        self.invertTree(root.left)
        self.invertTree(root.right)
        # Return root
        return root