import unittest
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        previous = None
        i=0
        while i < len(nums):
            num = nums[i]
            if previous == None:
                previous = num
                i += 1
            elif num <= previous:
                del nums[i]
            else:
                previous = num
                i+=1
        return len(nums)

class Test(unittest.TestCase):
    def test_1(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        result = Solution().removeDuplicates(nums)
        self.assertEqual(result,5)
        self.assertEqual(nums, [0,1,2,3,4])