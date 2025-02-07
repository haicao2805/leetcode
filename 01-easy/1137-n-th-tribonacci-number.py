class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]


class TLESolution:
    def tribonacci(self, n: int) -> int:
        def calc(n: int) -> int:
            if n == 0:
                return 0
            if n <= 2:
                return 1
            return calc(n - 1) + calc(n - 2) + calc(n - 3)

        return calc(n)
