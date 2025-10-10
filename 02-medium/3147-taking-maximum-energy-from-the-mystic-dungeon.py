from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [0 for _ in range(n)]

        for i in range(n - k, n):
            dp[i] = energy[i]

        for i in range(n - k - 1, -1, -1):
            dp[i] = energy[i] + dp[i + k]

        return max(dp)


if __name__ == "__main__":
    s = Solution()
    print(s.maximumEnergy(energy=[5, -200, -10, -5, 100], k=3))
    print(s.maximumEnergy(energy=[-2, -3, -1], k=2))
