from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        N = len(nums)
        pk = [0] * (N + 1)
        for i in range(N):
            pk[i + 1] = int(nums[i] == k) + pk[i]

        res = 0
        pv = [0] * (N + 1)
        for v in set(nums):
            for i in range(N):
                pv[i + 1] = int(nums[i] == v) + pv[i]

            lossK = 0
            for i in range(N):
                lossK = int(min(lossK, pv[i] - pk[i]))
                freKOnRight = pk[N] - pk[i + 1]
                freVOnLeft = pv[i + 1]
                res = max(res, freKOnRight + freVOnLeft - lossK)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.maxFrequency([10, 2, 3, 4, 5, 5, 4, 3, 2, 2], 10) == 4)
    print(s.maxFrequency([1, 2, 3, 4, 5, 6], 1) == 2)
    print(s.maxFrequency([10, 2, 2, 2, 10, 2], 10) == 5)
    print(s.maxFrequency([2, 8], 8) == 2)
    print(s.maxFrequency([1, 9], 8) == 1)
    print(s.maxFrequency([3, 8, 5, 3, 5, 2, 2], 8) == 3)
