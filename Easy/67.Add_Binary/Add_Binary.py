#!/usr/bin/env python3
from typing import *

#* All tests passed
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #* We convert the str binary representations to decimal integers
        aInt: int = int(a, 2)
        bInt: int = int(b, 2)
        #* We add both values
        sum: int = aInt + bInt
        #* We return the string representating the binary number of the sum. "[2:]" says that we want to cut the first two characters
        #* thats because bin() automatically puts "0b" at the start to say that it's a binary
        return bin(sum)[2:]

#* I don't like maths so no big brain solution // Don't work harder work smarter
