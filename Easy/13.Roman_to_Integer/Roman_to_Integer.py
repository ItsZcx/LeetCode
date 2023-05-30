#!/usr/bin/env python3
from typing import *

def validSubstraction(self, s: str, index: int) -> bool:
    if (s[index] == "I" and (s[index + 1] == "V" or s[index + 1] == "X")):
        return True
    if (s[index] == "X" and (s[index + 1] == "L" or s[index + 1] == "C")):
        return True
    if (s[index] == "C" and (s[index + 1] == "D" or s[index + 1] == "M")):
        return True
    return False


#* All tests passed
#* Beats 38% runtime and 23% memory
class Solution:
    def romanToInt(self, s: str) -> int:
        index: int = 0
        result: int = 0
        tempNum: int = 0
        #* Declaration of a dictionary with each roman letter and it's value
        romanValues: Dict(str, int) = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        while index < len(s):
            #* Checking for valid subtraction (two chars)
            if (index + 1 < len(s) and validSubstraction(Solution, s, index)):
                tempNum = romanValues[s[index + 1]] - romanValues[s[index]]
                index += 1
            #* Else just add it's value from the dictionary
            else:
                tempNum = romanValues[s[index]]
            result += tempNum
            index += 1
        return result


#* All tests passed
#* Beats 60% runtime and 54% memory
class Solution:
    def romanToInt(self, s: str) -> int:
        index: int = 0
        result: int = 0
        str_length: int = len(s)
        #* Declaration of a dictionary with each roman letter and it's value to use it as a hashmap
        romanValues: Dict(str, int) = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        #* Iteration through 0 and str_length
        for index in range(str_length):
            #* Condition to check if it's a substraction .Handled not to enter on last char.
            if (index < str_length - 1 and romanValues[s[index]] < romanValues[s[index + 1]]):
                #* Instead of adding the value of the roman number, ex: IV, we can just substract 1 from the result and then add
                #* the 5 in the next else, this way each operation is independent
                result -= romanValues[s[index]]
            else:
                result += romanValues[s[index]]
        return result
