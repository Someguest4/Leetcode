import unittest
from codewars_deaf_rats import count_deaf_rats

class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = """
        ↗ P     
          ↘    ↖
          ↑     
        ↗       
        """.strip("\n").split("\n")
        self.assertEqual(count_deaf_rats(s), 1)

        s = """
                ↗
        P ↓   ↖ ↑
            ←   ↓
          ↖ ↙   ↙
        ↓ ↓ ↓    
        """.strip("\n").split("\n")
        self.assertEqual(count_deaf_rats(s), 7)

        s = """
        ↘ ↓ ↙
        → P ←
        ↗ ↑ ↖
        """.strip("\n").split("\n")
        self.assertEqual(count_deaf_rats(s), 0)

        s = """
        ↖ ↑ ↗
        ← P →
        ↙ ↓ ↘
        """.strip("\n").split("\n")
        self.assertEqual(count_deaf_rats(s), 8)


if __name__ == '__main__':
    unittest.main()
