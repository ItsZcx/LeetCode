#!/usr/bin/env python3
from typing import *

#* Sort strings and compare
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        return s == t
