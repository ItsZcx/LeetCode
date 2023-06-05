#!/usr/bin/env python3
from typing import *

#* All tests passed
class Solution:
    def climbStairs(self, n: int) -> int:
        one: int = 1
        two: int = 0
        temp: int = 0

        #* Basically it's a fibonacci sequence. Go google
        for index in range(n):
            temp = one
            one = one + two
            two = temp
        return one
