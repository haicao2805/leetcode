from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        preSum = 0
        maxEnding = 0
        minEnding = 0

        for n in nums:
            preSum += n

            maxEnding = max(preSum, maxEnding)
            minEnding = min(preSum, minEnding)

        return int(abs(maxEnding)) + int(abs(minEnding))


if __name__ == "__main__":
    s = Solution()
    # print(s.maxAbsoluteSum([-1]))
    print(s.maxAbsoluteSum([1, -3, 2, 3, -9]))
    # print(s.maxAbsoluteSum([2, -5, 1, -4, 3, -2]))
    print(
        s.maxAbsoluteSum(
            [-3, -5, -3, -2, -6, 3, 10, -10, -8, -3, 0, 10, 3, -5, 8, 7, -9, -9, 5, -8]
        )
    )
# i = 0, preSum = 1, maxEnding = 1, minEnding = 1,
# i = 1,  = 2, preSum = 2, res = 3


#     1,-3, 2, 3, 9
# pre 1,-2, 0, 3,12
# min 1,-2,-2,-2,-2
# max 1, 1, 1, 3,12

#     1,-3, 2, 3,-9
# pre 1,-2, 0, 3,-6
# min 1,-2,-2,-2,-6
# max 1, 1, 1, 3, 3

1 2 3 -5 -5 -5

6
-9

class BruteForceSolution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        N = len(nums)
        preSum = [0] * N

        preSum[0] = nums[0]
        res = abs(preSum[0])
        for i in range(1, N):
            preSum[i] = preSum[i - 1] + nums[i]

        for i in range(N - 1):
            for j in range(i, N):
                if i == 0:
                    res = max(res, abs(preSum[j]))
                else:
                    res = max(res, abs(preSum[j] - preSum[i - 1]))

        return res
