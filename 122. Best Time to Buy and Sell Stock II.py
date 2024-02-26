from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = right = profit = 0
        for i in range(len(prices)):
            if prices[i] < prices[left]:
                left = i
                right = i
            elif prices[i] > prices[right]:
                right = i
            if prices[right] > prices[left]:
                right = i
                profit += prices[right] - prices[left]
                left = i
        return profit


solution = Solution()
assert solution.maxProfit([7,1,5,3,6,4]) == 7
assert solution.maxProfit([1,2,3,4,5]) == 4
assert solution.maxProfit([7,6,4,3,1]) == 0

