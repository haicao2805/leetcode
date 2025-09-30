from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            new_nums = list()
            for i in range(len(nums) - 1):
                new_nums.append((nums[i] + nums[i + 1]) % 10)
            nums = new_nums
        return nums[0]


if __name__ == "__main__":
    s = Solution()
    print(s.triangularSum([1, 2, 3, 4, 5]))
    print(s.triangularSum([5]))


class SolutionOne:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[0][i] = nums[i]

        for i in range(1, n):
            for j in range(i, n):
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % 10

        return dp[n - 1][n - 1]
