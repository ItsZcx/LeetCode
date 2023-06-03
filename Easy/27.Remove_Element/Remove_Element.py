#!/usr/bin/env python3
from typing import *

#* All tests passed (idk if 100% in-place)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #* Same idea as in the question 26.
        #* While there exists the value "val" in the array, remove it
        while nums.count(val) != 0:
            nums.remove(val)
        #* Numbers in array == numbers not "val"
        return len(nums)


#* All tests passed (100% in-place)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointerOne : int = 0
        pointerTwo : int = 0

        #* Same idea as question 26 second option.
        #* We iterate the array
        while pointerTwo < len(nums):
            #* If the value at pTwo is val, we will increment until it isn't
            if nums[pointerTwo] == val:
                pointerTwo += 1
            #* When it isn't, we will put that value at pOne and increment both values (this changes from the solution from q26
            #* because now we want to be able to remove a value at pos 0 and we also have to increment pTwo when we found a value
            #* that isn't val even thought it is the same as the one in the iteration before)
            else:
                nums[pointerOne] = nums[pointerTwo]
                pointerOne += 1
                pointerTwo += 1
            #* The amount of values not "val" == pOne
        return pointerOne
