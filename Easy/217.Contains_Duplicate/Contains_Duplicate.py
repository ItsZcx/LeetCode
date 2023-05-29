#!/usr/bin/env python3
from typing import *

#* Algorithm. 65 / 72 testcases passed
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        out_index: int = 0
        in_index: int = 0

        for out_index in range(len(nums)):
            for in_index in range(len(nums)):
                if out_index != in_index and nums[out_index] == nums[in_index]:
                    return True
        return False


#* Optimized algorithm. 65 / 72 testcases passed
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        out_index: int = 0
        in_index: int = 0

        for out_index in range(0, len(nums)):
            for in_index in range(out_index + 1, len(nums)):
                if nums[in_index] == nums[out_index]:
                    return True
        return False


#* Hash map. All tests passed
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        out_index: int = 0
        map: Dict[int, int] = {}

        for out_index in range(len(nums)):
            if nums[out_index] in map:
                return True
            map[nums[out_index]] = nums[out_index]
        return False
