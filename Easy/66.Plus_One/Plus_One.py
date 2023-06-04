#!/usr/bin/env python3
from typing import *

#* All tests passed
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        hasToIncrement: bool = True

        #* We iterate backwards the array
        for index in range(len(digits) - 1, -1, -1):
            #* In case we have to increment the value, and it's < 9, we just increment it and break the loop (we have finished)
            if digits[index] < 9 and hasToIncrement == True:
                digits[index] += 1
                hasToIncrement = False
                break
            #* In case we have to increment the value, and it's >= 9, we put the current value to 0 (9 -> 10 not acceptable), and we put "hasToIncrement" to true,
            #* that way we can go back to the first if condition or if it's the first position (last iteration), we will say that we have to insert a new number at the start
            elif hasToIncrement == True and digits[index] >= 9:
                hasToIncrement = True
                digits[index] = 0
        #* In case we have to insert a new number at the start (first position has value 9), we insert at index "0", the value "1"
        if hasToIncrement == True:
            digits.insert(0, 1)
        return digits
