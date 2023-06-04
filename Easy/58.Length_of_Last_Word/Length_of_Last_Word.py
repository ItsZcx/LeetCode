#!/usr/bin/env python3
from typing import *

#* All tests passed --- x/x passed
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count: int = 0
        #* We use "-1" because that way we can directly start at the end of the string and we dont have to count every word in case it's the final one
        index: int = -1

        #* We skip to the word in case there are spaces at the end
        while s[index] == " ":
            index -= 1
        #* Here we count until we find a space (the word has ended). "(index * -1) <= len(s)" Is error handling, so we don't go past the length of the string
        while (index * -1) <= len(s) and s[index] != " ":
            count += 1
            index -= 1
        return count
