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
    # Solution to "100. Same tree"
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q or p. val != q.val:
            return False
        return (self.isSameTree(p. left, q. left) and self.isSameTree(p. right, q.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Edge case
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        # Check if there is any subtree on root == "subRoot"
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))