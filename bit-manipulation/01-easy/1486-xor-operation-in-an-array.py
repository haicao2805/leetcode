class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + 2 * i for i in range(n)]

        res = 0
        for n in nums:
            res ^= n
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.xorOperation(5, 0))
