class Solution:
    def countGoodNumbers(self, n: int) -> int:
        return pow(5, (n + 1) // 2, 10**9 + 7) * pow(4, n // 2, 10**9 + 7) % (10**9 + 7)


class FirstSolution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def quickMul(x, y) -> int:
            ret, mul = 1, x
            while y > 0:
                if y & 1 == 1:
                    ret = ret * mul % MOD
                mul = mul * mul % MOD
                y //= 2
            return ret

        return quickMul(5, (n + 1) // 2) * quickMul(4, n // 2) % MOD


if __name__ == "__main__":
    s = Solution()
    print(s.countGoodNumbers(1))
    print(s.countGoodNumbers(4))
    print(s.countGoodNumbers(5))
    print(s.countGoodNumbers(50))
