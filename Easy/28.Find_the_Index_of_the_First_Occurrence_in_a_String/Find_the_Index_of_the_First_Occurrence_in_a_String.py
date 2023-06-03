#!/usr/bin/env python3
from typing import *

#* All tests passed (I mean...)
class Solution:
    def strStra(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


#* All tests passed (I mean...x2)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        indexReturn: ValueError | int = 0

        try:
            indexReturn = haystack.index(needle)
        except ValueError:
            indexReturn = -1
        return indexReturn


#* All tests passed (Now solution with some logic tought behind)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #* Declaration of some variables for readability + bit more optimized
        indexTemp: int = 0
        wordFound: bool = False
        lengthNeedle: int = len(needle)
        lengthHaystack: int = len(haystack)

        #* We start the general iteration trough haystack
        for haystackIndex in range(lengthHaystack):
            #* Case we are trying to search for a solution bigger than the amount of chars left to check are (pyhton kabooms)
            if lengthHaystack - lengthNeedle < haystackIndex:
                return -1
            #* There is no point on checking if it's the same word if the first character isn't already correct
            if haystack[haystackIndex] == needle[0]:
                #* Declaration of a temp so we don't modify the original "haystackIndex"
                indexTemp = haystackIndex
                #* Now we check for the word
                for needleIndex in range(lengthNeedle):
                    #* In case we find the word, when we exit the loop, "wordFound" == True
                    if haystack[indexTemp] == needle[needleIndex]:
                        wordFound = True
                    else:
                        wordFound = False
                        break
                    indexTemp += 1
                    #* We check if we found the word, if so, we return "haystackIndex" (the starting position)
                if wordFound == True:
                    return haystackIndex
        #* needle was not in haystack
        return -1
