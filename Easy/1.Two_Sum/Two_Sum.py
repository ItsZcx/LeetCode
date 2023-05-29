#!/usr/bin/env python3
from typing import *

# Double iteration. All tests passed
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out_index:int = 0
        in_index:int = 0

        for out_index in range(len(nums)):
            for in_index in range(len(nums)):
                if in_index != out_index and nums[out_index] + nums[in_index] == target:
                    return [out_index, in_index]
        return -1

# Double iteration with the second one starting at pos [out_index + 1]. All tests passed
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out_index:int = 0
        in_index:int = 0

        for out_index in range(len(nums)):
            for in_index in range(out_index + 1, len(nums)):
                if nums[out_index] + nums[in_index] == target:
                    return [out_index, in_index]
        return -1