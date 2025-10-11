from typing import Counter, List


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        power.sort()
        count = Counter(power)
        dp = [[i, k, count[k], 0] for i, k in enumerate(count.keys())]
        n = len(count)

        res = 0
        mx = 0
        j = 0
        for i in range(n):
            while j < i and dp[j][1] + 2 < dp[i][1]:
                mx = max(mx, dp[j][3])
                j += 1

            dp[i][3] = mx + dp[i][1] * dp[i][2]
            res = max(res, dp[i][3])

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.maximumTotalDamage(power=[4, 1, 1, 1, 2, 3]))
    print(s.maximumTotalDamage(power=[7, 1, 6, 6]))
