#!/usr/bin/env python3
from typing import *

#* All tests passed
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Hash map to store the nums and repetitions
        hashMap: Dict[int, int] = {}

        # Put numbers in hash map as well as how many there are of each
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        # Sort hashmap to have the most frequent last
        hashMap = sorted(hashMap.items(), key=lambda item:item[1])
        # Return the most recent number (last position)
        return hashMap[-1][0]

#* All tests passed
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # So basically if there are more than half (n/2) of the numbers, if the list is sorted
        # the item at the middle of the list will always be the one we are looking for
        nums = sorted(nums)
        return nums[len(nums) // 2]