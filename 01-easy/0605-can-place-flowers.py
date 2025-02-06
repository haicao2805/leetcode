from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if (
                flowerbed[i] == 0
                and (i == 0 or flowerbed[i - 1] == 0)
                and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            ):
                flowerbed[i] = 1
                n -= 1

        return n <= 0


if __name__ == "__main__":
    s = Solution()
    print(s.canPlaceFlowers([1, 0, 0, 0, 1], 2))
    print(s.canPlaceFlowers([1, 0, 0, 0, 1], 1))
    print(s.canPlaceFlowers([0, 0, 1, 0, 0], 1))
