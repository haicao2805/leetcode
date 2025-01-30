from collections import defaultdict, deque
from typing import List

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        res = 0

        adj = defaultdict(list)
        for [u, v] in edges:
            adj[u].append(v)
            adj[v].append(u)

        def getConnectedComponent(src: int):
            q = deque([src])
            component = set([src])
            while q:
                node = q.popleft()
                for nei in adj[node]:
                    if nei in component:
                        continue
                    q.append(nei)
                    component.add(nei)
                    visit.add(nei)
            return component

        def longestPath(src: int):
            q = deque([(src, 1)]) # (node, group)
            dist = {src: 1}

            while q:
                node, length = q.popleft()
                for nei in adj[node]:
                    if nei in dist:
                        if dist[nei] == length:
                            return -1
                        continue
                    q.append((nei, length + 1))
                    dist[nei] = length + 1
            return max(dist.values())


        for i in range(1, n + 1):
            if i in visit:
                continue

            visit.add(i)
            component = getConnectedComponent(i)
            maxCnt = 0
            for src in component:
                length = longestPath(src)
                if length == -1:
                    return -1
                maxCnt = max(maxCnt, length)
            res += maxCnt
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.magnificentSets(6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))
    print(s.magnificentSets(3, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))
