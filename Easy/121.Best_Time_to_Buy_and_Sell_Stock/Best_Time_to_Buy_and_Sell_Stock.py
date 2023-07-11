#!/usr/bin/env python3
from typing import *

#* 198 / 212 testcases passed
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bPos:   int = 0
        profit: int = 0

        # Basically brute forcing every possible transaction between days and saving the one with highest profit
        for bought in prices:
            # Updating the day we are at so we can ignore previous days in the next loop
            bPos += 1
            for sold in prices[bPos:]:
                # Calculations
                profit = max(profit, sold - bought)
        return profit

#* All tests passed
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize profit + pointer to the lowest price
        profit:      int = 0
        lowestPrice: int = 0

        # Haven't seen days so far so lowestPrice == first day
        lowestPrice = prices[0]
        # We iterate through prices
        for price in prices:
            # If we find a lower price that the one that we previously had, we update "lowestPrice"
            if price < lowestPrice:
                lowestPrice = price
            # Every time we check if we have found a new max profit. There is no problem in updating "lowestPrice" because
            # every time we update it we will have a previous profit(0 or one that we found) with the previous "lowestPrice"
            # saved and we will only check the following days after the new value
            profit = max(profit, price - lowestPrice)
        return profit

prices = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]
print (Solution.maxProfit(Solution, prices2))
