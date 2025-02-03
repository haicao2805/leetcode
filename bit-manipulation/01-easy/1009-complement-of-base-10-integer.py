class Solution:
    def bitwiseComplement(self, n: int) -> int:
        res = 0
        idx = 0

        if n == 0:
            return 1

        while n:
            res += pow(2, idx) if n & 1 == 0 else 0
            idx += 1
            n >>= 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.bitwiseComplement(5))
    print(s.bitwiseComplement(10))
