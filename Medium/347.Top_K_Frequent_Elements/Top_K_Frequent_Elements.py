#!/usr/bin/env python3
from typing import *

#* All tests passed
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # {num, times seen}
        hashMap:  Dict[int, int] = {}
        solution: List[str] = []

        # Put in the map every number and increment it's value every time we find it again in the array
        for num in nums:
            if num not in hashMap: # put new num
                hashMap[num] = 1
            else: # increment times seen
                hashMap[num] += 1
        # We want to sort the hash map in reversed order (3, 2, 1...) so after
        # we can iterate k times and put those numbers on a list that we will return
        hashMap = sorted(hashMap.items(), key=lambda numItem:numItem[1], reverse=-1) # key expects a function that returns the values that we want the list to be sorted by
        for i in range(0, k):
            solution.append(hashMap[i][0])
        return solution

#* All tests passed.
# Other optimal solution O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a dictionary to store the count of each number
        count:  Dict[int, int] = {}

        # Create a list of empty lists to store numbers based on their frequency
        freq = [[] for i in range(len(nums) + 1)]

        # Count the occurrences of each number in the input list
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Store numbers in the 'freq' list based on their frequency
        for n, c in count.items():
            freq[c].append(n)

        # Create a result list to store the top k frequent numbers
        res = []

        # Traverse the 'freq' list from the end to start
        for i in range(len(freq) - 1, 0, -1):
            # Traverse each number in the current frequency bucket
            for n in freq[i]:
                # Append the number to the result list
                res.append(n)

                # Check if the result list has reached k numbers
                if len(res) == k:
                    return res

        # Return the result list containing the top k frequent numbers
        return res