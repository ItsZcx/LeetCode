#!/usr/bin/env python3
from typing import *

#* Prev solution to question: 242.Valid_Anagram
def isAnagram(self, s: str, t: str) -> bool:
    if (len(s) != len(t)):
        return False
    s = sorted(s)
    t = sorted(t)
    return s == t

#* Check if a string is inside an array of strings
def stringInArray(finalArray: List[List[str]], str:str) -> bool:
    inIndex:int = 0
    outIndex:int = 0

    for outIndex in range(len(finalArray)):
        for inIndex in range(len(finalArray[outIndex])):
            if (str == finalArray[outIndex][inIndex]):
                return False
    return True

#* 111 / 118 testcases passed
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        inIndex = 0
        outIndex = 0
        finalArray:List[List[str]] = []
        tempArray:List[str] = []

        for outIndex in range(len(strs)):
            for inIndex in range(len(strs)):
                #* Check if "strs[inIndex]"" is an anagram and if it's not already inside finalArray
                if (isAnagram(Solution, strs[outIndex], strs[inIndex]) == True and
                stringInArray(finalArray, strs[inIndex]) == True):
                    tempArray.append(strs[inIndex])
            #* Store "tempArray" if it isnt empty
            if (len(tempArray) > 0):
                finalArray.append(tempArray)
            tempArray = []
        return finalArray

#* All tests passed
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #* Create a dictionary to act as hashmap
        res: Dict[int, int] = {}
        #* Visualization of a dictionary
        # res = {
        #   "brand": "Ford", --> key: values
        #   "model": "Mustang",
        #   "year": 1964
        # }
        for word in strs:
            #* We store the sorted word in "tempKey", take into cosideration that for the same anagram group, every single possible word
            #* will have the same sorted output
            # "sorted" returns a list but we want to store a string into tempKey. The function ''.join will concatenate
            # '' with the list as a string, basically doing the conversion list -> string
            tempKey = ''.join(sorted(word))
            #* If the sorted word (tempKey) exists in the dictionary (it's anagram group exists), append to the "values" part of the dictionary the "word"
            if tempKey in res:
                # with res[tempKey] we are accesing to the "values" part of the dictionary located at the key "tempKey"
                res[tempKey].append(word)
            #* Else, add a new key-value pair to the dictionary
            else:
                # if "res[tempKey]" doesn't exist it will create it's key and then add its value
                res[tempKey] = [word]
        #* With .values we are returning only the values from the dictionary
        return res.values()