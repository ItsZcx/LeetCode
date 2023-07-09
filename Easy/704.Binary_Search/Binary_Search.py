#!/usr/bin/env python3
from typing import *

#* All tests passed (Binary search algo)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        midPos:   int = 0
        leftPos:  int = 0
        rightPos: int = len(nums) - 1

        # We loop until the left pointer has surpased the right one (no solution)
        while leftPos <= rightPos:
            # We calculate new middle position.
                # same as (rightPos + leftPos // 2) but in some languages that can overflow (not python but just so I remember)
            midPos = leftPos + ((rightPos - leftPos) // 2)
            # If the target is in the right side or its not in the list but > than the last number,
            # leftPos -> midPos + 1 (target is not in the values <= midPos)
            if nums[midPos] < target:
                leftPos = midPos + 1
            # If the target is in the left side or its not in the list but < than the last number,
            # rightPos -> midPos - 1 (target is not in the values >= midPos)
            elif nums[midPos] > target:
                rightPos = midPos - 1
            # Solution found (nums[midPos] == target)
            else:
                return midPos
            # No solution
        return -1

print(Solution.search(Solution, [0,1,2,3,4,5,6,7,8,9,10], 8))