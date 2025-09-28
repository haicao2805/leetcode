from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(n - 3, -1, -1):
            if nums[i] + nums[i + 1] > nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0


if __name__ == "__main__":
    s = Solution()
    print(s.largestPerimeter([4, 5, 9, 9, 10, 10]))


class TLESolution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        def isTriangle(i: int, j: int, k: int) -> bool:
            if nums[i] + nums[j] <= nums[k]:
                return False
            if nums[k] + nums[j] <= nums[i]:
                return False
            if nums[i] + nums[k] <= nums[j]:
                return False
            return True

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if isTriangle(i, j, k):
                        res = max(res, nums[i] + nums[j] + nums[k])

        return res
