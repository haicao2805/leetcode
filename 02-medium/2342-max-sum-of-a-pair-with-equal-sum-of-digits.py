from typing import DefaultDict, List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sumOfDigits(n: int) -> int:
            s = 0
            while n:
                s += n % 10
                n = int(n / 10)
            return s

        hmap = [0] * 82
        res = -1
        for n in nums:
            sumDigit = sumOfDigits(n)

            if hmap[sumDigit]:
                res = max(res, hmap[sumDigit] + n)

            hmap[sumDigit] = max(hmap[sumDigit], n)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.maximumSum([18, 43, 36, 13, 7]))
    print(s.maximumSum([10, 12, 19, 14]))


class TLESolution:
    def maximumSum(self, nums: List[int]) -> int:
        def sumOfDigits(n: int) -> int:
            s = 0
            while n:
                s += n % 10
                n = int(n / 10)
            return s

        hmap = DefaultDict(list)
        res = -1
        for n in nums:
            sumDigit = sumOfDigits(n)

            if sumDigit in hmap:
                for v in hmap[sumDigit]:
                    res = max(res, n + v)

            hmap[sumDigit].append(n)

        return res
