from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = 0
        for candy in candies:
            maxCandies = max(maxCandies, candy)

        res = [False] * len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandies:
                res[i] = True
            else:
                res[i] = False
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.kidsWithCandies([2, 3, 5, 1, 3], 3))
    print(s.kidsWithCandies([4, 2, 1, 1, 2], 1))
