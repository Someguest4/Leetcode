import unittest
from typing import List


class Solution:
    def gcd(self, a, b):
        remainder = a % b
        if remainder != 0:
            return self.gcd(b, remainder)
        else:
            return b

    def countBeautifulPairs(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                a = int(str(nums[i])[0])
                b = int(str(nums[j])[-1])
                if a > b:
                    gcd = self.gcd(a, b)
                else:
                    gcd = self.gcd(b, a)
                if gcd == 1:
                    result += 1
        return result


class Testcase(unittest.TestCase):
    def test1(self):
        result = Solution().countBeautifulPairs(nums=[2, 5, 1, 4])
        self.assertEqual(result, 5)

    def test2(self):
        result = Solution().countBeautifulPairs(nums=[11, 21, 12])
        self.assertEqual(result, 2)
