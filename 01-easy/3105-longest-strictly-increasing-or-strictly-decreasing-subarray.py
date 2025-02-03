from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        increasingArr = [1] * N
        decreasingArr = [1] * N

        res = 1
        for i in range(1, N):
            if nums[i] > nums[i - 1]:
                increasingArr[i] = increasingArr[i - 1] + 1

            if nums[i] < nums[i - 1]:
                decreasingArr[i] = decreasingArr[i - 1] + 1

            res = max(res, increasingArr[i], decreasingArr[i])

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.longestMonotonicSubarray([1, 3, 5, 4, 7]))
    print(s.longestMonotonicSubarray([1, 4, 3, 3, 2]))
    print(s.longestMonotonicSubarray([3, 3, 3, 3]))
    print(s.longestMonotonicSubarray([3, 2, 1]))
