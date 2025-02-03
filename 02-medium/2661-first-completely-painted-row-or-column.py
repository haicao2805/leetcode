from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows, cols, hmap = {}, {}, {}

        ROWS, COLS = len(mat), len(mat[0])

        for r in range(ROWS):
            rows[r] = 0
        for r in range(COLS):
            cols[r] = 0
        for r in range(ROWS):
            for c in range(COLS):
                hmap[mat[r][c]] = (r, c)

        for i, n in enumerate(arr):
            r, c = hmap[n]
            rows[r] += 1
            cols[c] += 1

            if rows[r] == COLS:
                return i
            if cols[c] == ROWS:
                return i

        return 0


if __name__ == "__main__":
    s = Solution()
    print(s.firstCompleteIndex([1, 3, 4, 2], [[1, 4], [2, 3]]) == 2)
    print(
        s.firstCompleteIndex(
            [2, 8, 7, 4, 1, 3, 5, 6, 9], [[3, 2, 5], [1, 4, 6], [8, 7, 9]]
        )
        == 3
    )
    print(
        s.firstCompleteIndex(
            [8, 2, 4, 9, 3, 5, 7, 10, 1, 6], [[8, 2, 9, 10, 4], [1, 7, 6, 3, 5]]
        )
        == 5
    )
