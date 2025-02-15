class Solution:
    def punishmentNumber(self, n: int) -> int:
        def canPartition(n: int, target: int) -> bool:
            if target < 0 or n < target:
                return False
            if n == target:
                return True

            return (
                canPartition(n // 10, target - n % 10)
                or canPartition(n // 100, target - n % 100)
                or canPartition(n // 1000, target - n % 1000)
            )

        res = 0
        for i in range(1, n + 1):
            if canPartition(i * i, i):
                res += i * i

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.punishmentNumber(10))
    print(s.punishmentNumber(37))
