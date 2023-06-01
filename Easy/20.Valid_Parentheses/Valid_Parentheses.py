#!/usr/bin/env python3
from typing import *

#*All tests passed (ugly solution)
class Solution:
    def isValid(self, s: str) -> bool:
        #* We create the stack
        stack: List = []

        #* We append first position because we are gonna use "index + "1 so we have to put the range to "len(s) - 1"
        stack.append(s[0])
        for index in range(len(s) - 1):
            stack.append(s[index + 1])
            #* Check for pairs in the stack, if there are, pop them both
            if (len(stack) > 2 and
            (stack[-2] == "(" and stack[-1] == ")" or
            stack[-2] == "[" and stack[-1] == "]" or
            stack[-2] == "{" and stack[-1] == "}")):
                stack.pop()
                stack.pop()
        #* Check for pairs again cuz idk I messed up and there was always a pair missing in some cases
        if (len(stack) == 2 and
        (stack[-2] == "(" and stack[-1] == ")" or
        stack[-2] == "[" and stack[-1] == "]" or
        stack[-2] == "{" and stack[-1] == "}")):
            stack.pop()
            stack.pop()
        #* If the stack is empty, they were all pairs
        if len(stack) == 0:
            return True
        return False

# *All tests passed (better)
class Solution:
    def isValid(self, s: str) -> bool:
        #* We create the stack, dictionary and several arrays with possible brackets
        stack: List = []
        opening: List = ["(", "[", "{"]
        closing: List = [")", "]", "}"]
        pairs: Dict(str, str) = {"(": ")", "[": "]", "{": "}"}

        #* We iterate through the string
        for char in s:
            #* For every single iteration we check if it's an opening bracket. If it is, we put it at the top of the stack
            if char in opening:
                stack.append(char)
            #* Else if it's a closing bracket..
            elif char in closing:
                #* If the stack is empty we return False. Reason: if we are at a closing bracket and there are no opening brackets -> "...]" == no pair for the bracket.
                #* If the stack is not empty (there is an opening bracket) and the character we are at isn't it's corresponding pair, we return False
                if not stack or pairs[stack.pop()] != char: # stack.() returns the stack character, pairs[stackChar] uses "stackChar" as the key and checks if its value(closing bracket) != char
                    return False
        #* If the stack is empty, they were all pairs
        if len(stack) == 0:
            return True
        return False
