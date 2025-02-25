class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.hammingWeight(11))
    print(s.hammingWeight(128))
    print(s.hammingWeight(2147483645))
