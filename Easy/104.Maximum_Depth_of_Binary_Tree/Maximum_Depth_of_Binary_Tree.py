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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If no node return depth 0 (don't increment depth)
        if not root:
            return 0

        # Save depth of childs
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        # Return highest depth + 1 (we go up until root node so +1+1+1...maxDepth)
        if leftDepth >= rightDepth:
            return leftDepth + 1
        if rightDepth > leftDepth:
            return rightDepth + 1

#* All tests passed
# Same thing as above but diff syntax
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # Return highest depth + 1 (we go up until root node so +1+1+1...maxDepth)
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))