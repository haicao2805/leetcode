from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) + 1):
            res ^= i
        for n in nums:
            res ^= n
        return res


class SolutionFormula:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        return total - sum(nums)


class SolutionHashMap:
    def missingNumber(self, nums: List[int]) -> int:
        hmap = {}
        for n in nums:
            hmap[n] = 1

        res = -1
        for i in range(len(nums) + 1):
            if not hmap.get(i):
                res = i
                break
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.missingNumber([3, 0, 1]))
    print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(0 ^ 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6 ^ 7 ^ 8 ^ 9 ^ 0 ^ 1 ^ 2 ^ 3 ^ 5 ^ 6 ^ 7 ^ 8 ^ 9)
