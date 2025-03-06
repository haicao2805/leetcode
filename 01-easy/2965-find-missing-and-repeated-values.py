class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        N = len(grid)
        a, b = 0, 0
        hmap = {}
        for nums in grid:
            for n in nums:
                if n not in hmap:
                    hmap[n] = 1
                else:
                    a = n
        for i in range(1, N * N + 1):
            if i not in hmap:
                b = i

        return [a, b]


if __name__ == "__main__":
    s = Solution()
    print(s.findMissingAndRepeatedValues([[1, 3], [2, 2]]))
    print(s.findMissingAndRepeatedValues([[9, 1, 7], [8, 9, 2], [3, 4, 6]]))
