import unittest


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        result = -1
        j = 0
        for i in range(len(haystack)):
            if len(needle) % 2 == 0:
                word = haystack[j:i + len(needle)]
            else:
                word = haystack[j:i + len(needle)]
            j += 1
            if word == needle:
                result = i
                return result
        return result


class Test(unittest.TestCase):
    def test1(self):
        haystack = "sadbutsad"
        needle = "sd"
        result = Solution().strStr(haystack, needle)
        self.assertEqual(haystack.find(needle), result)
