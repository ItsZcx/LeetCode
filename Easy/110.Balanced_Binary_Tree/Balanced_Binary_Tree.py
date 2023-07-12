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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> List[Union[bool, int]]:
            # If there is no node return True (Balanced) and height 0
            if not node:
                return [True, 0]

            # Check childs for unbalanced nodes and height
            childLeft:  TreeNode = dfs(node.left)
            childRight: TreeNode = dfs(node.right)
            # Check if any child has an unbalanced node (childLeft[0] and childRight[0]) and then check that the current node isnt
            # unbalanced (abs(childLeft[1] - childRight[1]) <= 1)
            balanced:   bool = (childLeft[0] and childRight[0]) and (abs(childLeft[1] - childRight[1]) <= 1)
            # In case any prev nodes were unbalanced or the current one is we will return "[False, height]"
            return [balanced, 1 + max(childLeft[1], childRight[1])]
            # If we had one False in any node, after that every evaluation will become False so we only have to return the boolean
        return(dfs(root)[0])