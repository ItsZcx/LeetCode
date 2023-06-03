#!/usr/bin/env python3
from typing import *

#* All tests passed (idk if 100% in-place)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #* We store the value at the indexed position on num
        for num in nums:
            #* While there are more than 1 number in the array with the value of "num", we remove the first one in the array
            while nums.count(num) > 1:
                nums.remove(num)
        return len(nums) #* We are asked for the amount of unique numbers so we only have to return the length of the array


#! TWO POINTERS SOLUTION (100% in-place)

#* All tests passed
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointerOne: int = 0
        pointerTwo: int = 1
        numsLength: int = len(nums)

        #* Basic iteration
        while pointerTwo < numsLength:
            #* We increment pTwo for every repetition of numbers. Basically we will have this -> [pOne(value = 1), numbers(all values 1), pTwo(value != 1)]
            if nums[pointerOne] == nums[pointerTwo]:
                pointerTwo += 1
            #* After we have this: [pOne(value = 1), numbers(all values 1), pTwo(value != 1)], to the next position of pOne(value = 1), we put the value of pTwo(value != 1). Then we start again the codition above
            else:
                pointerOne += 1
                nums[pointerOne] = nums[pointerTwo]
            #* pOne will have the position of the last non repeated value in the array so if we add 1(array starts at 0) we have the amount of unique values
        return pointerOne + 1
