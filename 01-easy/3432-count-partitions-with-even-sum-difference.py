from typing import List

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        N = len(nums)
        preSum = [0 for _ in range(N)]
        for i, n in enumerate(nums):
            preSum[i] += n + (0 if i == 0 else preSum[i - 1])

        res = 0
        for i in range(N - 1):
            leftSum = preSum[i]
            rightSum = preSum[-1] - preSum[i]

            if abs(leftSum - rightSum) % 2 == 0:
                res += 1

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.countPartitions([10,10,3,7,6]))
    print(s.countPartitions([2,4,6,8]))
    print(s.countPartitions([1,2,2]))
