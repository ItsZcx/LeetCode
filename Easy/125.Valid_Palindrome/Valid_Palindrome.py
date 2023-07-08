#!/usr/bin/env python3
from typing import *

#* All tests passed
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lastPointer: int = 0
        firstPointer: int = 0

        # Modify string to lowercase + remove non alphannumerical characters
        s = s.lower()
        s = ''.join(filter(str.isalnum, s))
        lastPointer = len(s) - 1

        # Use two pointer to compare its "contrary" character
        while firstPointer < len(s):
            # If they are not the same return false
            if s[firstPointer] != s[lastPointer]:
                return False
            lastPointer -= 1
            firstPointer += 1
        # If its a palindrome return true
        return True


#* All tests passed
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lastPointer: int = 0
        firstPointer: int = 0

        s = s.lower()
        s = ''.join(filter(str.isalnum, s))
        lastPointer = len(s) - 1

        # Same thing as above but only go until half the string (already checked every character with its "contrary")
        while firstPointer < int(len(s) / 2):
            if s[firstPointer] != s[lastPointer]:
                return False
            lastPointer -= 1
            firstPointer += 1
        return True

#* All tests passed
class Solution:
    def isPalindrome(self, s: str) -> bool:
        firstPointer = 0
        lastPointer = len(s) - 1

        # This is the same as "while firstPointer < int(len(s) / 2):" without calling unnecessary functions
        while firstPointer < lastPointer:
            # We check the same way as in the previous solutions but in this example we ignore the
            # non alphanumerical characters (before we used functions to clean the string)
            while firstPointer < lastPointer and not self.alphanum(s[firstPointer]):
                firstPointer += 1
            while firstPointer < lastPointer and not self.alphanum(s[lastPointer]):
                lastPointer -= 1
            # Check if the alphanumerical "contrary" characters arent the same
            if s[firstPointer].lower() != s[lastPointer].lower():
                return False
            firstPointer += 1
            lastPointer -= 1
        return True