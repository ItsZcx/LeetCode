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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(pNode: TreeNode, qNode: TreeNode) -> bool:
            # If both nodes dont exist, they are the "same" node, null
            if not pNode and not qNode:
                return True
            # If both nodes exist and the values are the same we want to check the childrens
            if pNode and qNode and pNode.val == qNode.val:
                return min(dfs(pNode.left, qNode.left), dfs(pNode.right, qNode.right)) # min with booleans will always return False if there is one
            # If both nodes exist and the values arent the same, they are not the same node
            return False
        return dfs(p, q)

#* All tests passed
class Solution:
    # Same solution but better writting
    def isSameTree (self, p: TreeNode, q: TreeNode) -> bool:
        # If both nodes dont exist, they are the "same" node, null
        if not p and not q:
            return True
        # If one of the nodes doesnt exist or both of them exist but val1 != val2, they are not the same
        if not p or not q or p. val != q.val:
            return False
        # Check childrens
        return (self. isSameTree(p. left, q. left) and self. isSameTree(p. right, q.right))