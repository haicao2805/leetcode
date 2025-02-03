from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)
        preSum = [0 for _ in range(N + 1)]

        for i in range(N):
            preSum[i + 1] = preSum[i] + nums[i]

        for i in range(N):
            if preSum[i] == preSum[-1] - preSum[i + 1]:
                return i

        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.pivotIndex([2, 1, -1]))
