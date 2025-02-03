from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        res = []
        safeNodes = {}

        def dfs(node: int):
            if node in safeNodes:
                return safeNodes[node]
            safeNodes[node] = 0
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return 0
            safeNodes[node] = 1
            return 1

        for i in range(N):
            if dfs(i):
                res.append(i)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]))
    print(s.eventualSafeNodes([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]))
    print(s.eventualSafeNodes([[], [0, 2, 3, 4], [3], [4], []]))
