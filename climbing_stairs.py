import unittest
class Solution:
    def climbStairs(self, n: int) -> int:
        nums=[0,1,2]
        for i in range(3,n+1):
            nums.append(nums[i-1]+nums[i-2])

        result = nums[n]
        print(nums)
        return result



class Test(unittest.TestCase):
    def test1(self):
        n=1
        result = Solution().climbStairs(n)
        self.assertEqual(result,1)

    def test2(self):
        n = 2
        result = Solution().climbStairs(n)
        self.assertEqual(result, 2)

    def test3(self):
        n = 3
        result = Solution().climbStairs(n)
        self.assertEqual(result, 3)

    def test4(self):
        n = 4
        result = Solution().climbStairs(n)
        self.assertEqual(result, 5)

    def test5(self):
        n = 5
        result = Solution().climbStairs(n)
        self.assertEqual(result, 8)

    def test6(self):
        n = 6
        result = Solution().climbStairs(n)
        self.assertEqual(result, 13)

    def test7(self):
        n = 7
        result = Solution().climbStairs(n)
        self.assertEqual(result, 21)

    def test8(self):
        n = 8
        result = Solution().climbStairs(n)
        self.assertEqual(result, 34)
