from typing import List
import heapq

class DijsktraSolution:
    def minCost(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        R, L, B, T = 1, 2, 3, 4

        hmap = {}

        def isValidPair(i: int, j: int):
            return i >= 0 and i <= n -1 and j >= 0 and j <= m - 1

        for i in range(n):
            for j in range(m):
                if isValidPair(i+1,j):
                    hmap[(i,j) , (i+1,j)] = 0 if grid[i][j] == B else 1

                if isValidPair(i-1,j):
                    hmap[(i,j) , (i-1,j)] = 0 if grid[i][j] == T else 1

                if isValidPair(i,j+1):
                    hmap[(i,j) , (i,j+1)] = 0 if grid[i][j] == R else 1

                if isValidPair(i,j-1):
                    hmap[(i,j) , (i,j-1)] = 0 if grid[i][j] == L else 1


        pq = []
        dist = {}
        for i in range(n):
            for j in range(m):
                dist[(i, j)] = float('inf')
        dist[(0, 0)] = 0

        heapq.heappush(pq, (0, (0, 0)))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while pq:
            current_cost, (i, j) = heapq.heappop(pq)

            if (i, j) == (n - 1, m - 1):
                return current_cost

            if current_cost > dist[(i, j)]:
                continue

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if ((i, j), (ni, nj)) in hmap:
                    cost = hmap[((i, j), (ni, nj))]
                    new_cost = current_cost + cost
                    if new_cost < dist[(ni, nj)]:
                        dist[(ni, nj)] = new_cost
                        heapq.heappush(pq, (new_cost, (ni, nj)))

        return n - m - 2

if __name__ == "__main__":
    s = DijsktraSolution()
    print(s.minCost([[1,1,3], [3,2,2], [1,1,4]]))
    print(s.minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]))
    print(s.minCost([[1,1,3],[3,2,2],[1,1,4]]))
    print(s.minCost([[1,2],[4,3]]))
