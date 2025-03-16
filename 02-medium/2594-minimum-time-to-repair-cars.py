import math


class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        L, R = 0, min(ranks) * cars * cars

        def check(x: int) -> bool:
            return sum(int(math.sqrt(x / r)) for r in ranks) >= cars

        while L <= R:
            M = L + (R - L) // 2
            if check(M):
                R = M - 1
            else:
                L = M + 1

        return L


if __name__ == "__main__":
    s = Solution()
    print(s.repairCars([4, 2, 3, 1], 10))
    print(s.repairCars([5, 1, 8], 6))
