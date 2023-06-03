#!/usr/bin/env python3
from typing import *

#* All tests passed
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        oneBeforeTargetPos: int = -1

        #* We iterate trough the array
        for index in range(len(nums)):
            #* At the end, here, we will have the index of the number that is smaller than the target and has the closest value to it
            if nums[index] < target:
                oneBeforeTargetPos = index
            #* We found target so we return the position were it is
            if nums[index] == target:
                return index
        #* We return the position + 1 because target has to be after the number in that position
        return oneBeforeTargetPos + 1
