from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        n = len(nums1)
        m = len(nums2)

        if m % 2 != 0:
            for i in nums1:
                res ^= i

        if n % 2 != 0:
            for i in nums2:
                res ^= i

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.xorAllNums([2, 1, 3], [10, 2, 5, 0]))
    print(s.xorAllNums([1, 2], [3, 4]))
