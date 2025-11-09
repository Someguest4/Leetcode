import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxs = self.find_maxs(prices)
        max_profit = 0

        for i in range(len(prices)):
            profit =maxs[i] - prices[i]
            max_profit = max(max_profit, profit)

        return max_profit

    def find_maxs(self, prices: List[int]) -> List[int]:
        maxs = []
        for i in range(len(prices)-1, -1, -1):
            if not maxs:
                maxs.append(prices[i])
            else:
                maxs.append(max(maxs[len(maxs) - 1], prices[i]))
        return maxs[::-1]

class Test(unittest.TestCase):
    def test1(self):
        prices = [8, 9, 1, 3, 5, 7]
        result = Solution().maxProfit(prices)
        self.assertEqual(result, 6)

    def test2(self):
        prices = [7,1,2,5,3,6,4]
        result= Solution().maxProfit(prices)
        self.assertEqual(result,5)

    def test3(self):
        prices = [7,6,4,3,1]
        result = Solution().maxProfit(prices)
        self.assertEqual(result, 0)
    def test4(self):
        prices = [2,9,1,3,5,7]
        result = Solution().maxProfit(prices)
        self.assertEqual(result, 7)