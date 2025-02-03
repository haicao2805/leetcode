from collections import deque
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        adj: dict[int, set[int]] = {}

        def bfs(start: int, visit: List[bool]):
            q = deque()
            q.append((start, 0))

            while q:
                (node, parent) = q.popleft()
                visit[node] = True

                for nei in adj.get(node, []):
                    if visit[nei] and nei != parent:
                        return True
                    if nei == parent:
                        continue

                    visit[nei] = True
                    q.append((nei, node))

        for [u, v] in edges:
            if u not in adj:
                adj[u] = set()
                adj[u].add(v)
            else:
                adj[u].add(v)

            if v not in adj:
                adj[v] = set()
                adj[v].add(u)
            else:
                adj[v].add(u)

            visit = [False for _ in range(N + 1)]
            if bfs(u, visit):
                return [u, v]

        return []


if __name__ == "__main__":
    s = Solution()
    print(s.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
    print(s.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
