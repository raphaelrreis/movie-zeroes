import unittest

from Solution import Solution
class TestSolution(unittest.TestCase):
    def test_moveZeroes(self):
        solution = Solution()

        nums1 = [0, 1, 0, 3, 12]
        solution.moveZeroes(nums1)
        self.assertEqual(nums1, [1, 3, 12, 0, 0])

        nums2 = [0, 0, 1]
        solution.moveZeroes(nums2)
        self.assertEqual(nums2, [1, 0, 0])

        nums3 = [1, 2, 3, 4, 5]
        solution.moveZeroes(nums3)
        self.assertEqual(nums3, [1, 2, 3, 4, 5])

        nums4 = [0, 0, 0, 0, 0]
        solution.moveZeroes(nums4)
        self.assertEqual(nums4, [0, 0, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()
