#!/usr/bin/env python3
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#* 100/104 passed
# Though that the two logest 2 depths added would find it but it isn't true in all cases
class Solution:
    def dfs(self, node: Optional[TreeNode], depth: int) -> int:
        if not node:
            return 0
        return 1 + max(Solution.dfs(self, node.left, depth + 1), Solution.dfs(self, node.right, depth + 1))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        rightDepth: int = 0
        leftDepth:  int = 0
        if root.left:
            leftDepth = self.dfs(root.left, 0)
        if root.right:
            rightDepth = self.dfs(root.right, 0)
        return leftDepth + rightDepth

#* All tests passed
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(root):
            nonlocal diameter
            # If there is no node, value of Height is -1 (that way we can say that the last node has Height == 0 (we return 1 + Height(value 0)))
            if not root:
                return -1
            # We search for the max height in x node childrens...
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)
            # While we are doing that we calculate the diameter of x node, in case its bigger than the prev max diameter we update it
            # (We have to add 2 because every null node is -1, that way if we have one child, diameter is 2 + 1(non null child) - 1(null child) = 2(non null child and root))
            diameter = max(diameter, 2 + leftHeight + rightHeight)

            return 1 + max(leftHeight, rightHeight)

        # Call recusion and return updated diameter
        dfs(root)
        return diameter
    # Btw checking if the diameter was bigger in every node was what I was missing in the one above