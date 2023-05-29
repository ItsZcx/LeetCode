#!/usr/bin/env python3
from typing import *

#* All tests passed
#* Beats 34% runtime, 14% memory
class Solution:
    def isPalindrome(self, x: int) -> bool:
        leftPointer = 0
        intStr:str = str(x)
        rigthPointer = len(intStr) - 1

        #* Only one char -> palindrome
        if (x < 10 and x > -1):
            return True
        #* Compare the 2 side chars with each other until the middle of the string.
        # (already tested every single case, if we kept going we would do every case two times)
        while leftPointer < len(intStr) / 2:
            if (intStr[leftPointer] != intStr[rigthPointer]):
                return False
            leftPointer += 1
            rigthPointer -= 1
        return True


#* All tests passed.
#* Beats 60% runtime, 43% memory
class Solution:
    def isPalindrome(self, x: int) -> bool:
        intStr:str = str(x)
        reversedIntStr:str = "".join(reversed(intStr))

        if intStr != reversedIntStr:
            return False
        return True
