from heapq import heappop, heappush
from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        ROWS, COLS = len(heightMap), len(heightMap[0])
        VISITED = -1

        minHeap = []
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1:
                    heappush(minHeap, (heightMap[r][c], r, c))
                    heightMap[r][c] = VISITED


        res = 0
        maxHeight = 0

        while minHeap:
            h, r, c = heappop(minHeap)
            maxHeight = max(maxHeight, h)
            res += maxHeight - h

            neighbors = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]
            for nr, nc in neighbors:
                if 0 <= nr <= ROWS - 1 and 0 <= nc <= COLS - 1 and heightMap[nr][nc] != VISITED:
                    heappush(minHeap, (heightMap[nr][nc], nr, nc))
                    heightMap[nr][nc] = VISITED

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]])) # 4
    print(s.trapRainWater([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]))
