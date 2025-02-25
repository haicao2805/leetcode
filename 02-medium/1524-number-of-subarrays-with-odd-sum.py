from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = 0
        preSum = 0
        odd = 0
        even = 0
        MOD = 1_000_000_007

        for n in arr:
            preSum += n

            if preSum % 2 == 1:
                res = (res + 1 + even) % MOD
                odd += 1

            else:
                res = (res + odd) % MOD
                even += 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.numOfSubarrays([1, 3, 5]))
    print(s.numOfSubarrays([2, 4, 6]))
    print(s.numOfSubarrays([1, 2, 3, 4, 5, 6, 7]))
