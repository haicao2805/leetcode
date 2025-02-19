from collections import defaultdict, deque
from typing import List


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        N = len(favorite)
        longestCycle = 0
        visit = [False] * N
        lengthTwoCycles = []

        # 1. Find the longest cycle
        for i in range(N):
            if visit[i]:
                continue

            start, cur = i, i
            curSet = set()

            while not visit[cur]:
                visit[cur] = True
                curSet.add(cur)
                cur = favorite[cur]

            if cur in curSet:
                length = len(curSet)
                while start != cur:
                    length -= 1
                    start = favorite[start]
                longestCycle = max(longestCycle, length)
                if length == 2:
                    lengthTwoCycles.append([cur, favorite[cur]])

        # 2. Find sum of longest non-closed circles
        inverted = defaultdict(list)
        for dst, src in enumerate(favorite):
            inverted[src].append(dst)

        def bfs(src: int, parent: int):
            q = deque([(src, 0)])
            maxLength = 0

            while q:
                node, length = q.popleft()
                if node == parent:
                    continue
                maxLength = max(maxLength, length)
                for nei in inverted[node]:
                    q.append((nei, length + 1))

            return maxLength

        chainSum = 0
        for n1, n2 in lengthTwoCycles:
            chainSum += bfs(n1, n2) + bfs(n2, n1) + 2

        return max(chainSum, longestCycle)


if __name__ == "__main__":
    s = Solution()
    print(s.maximumInvitations([2, 2, 1, 2]) == 3)
    print(s.maximumInvitations([1, 2, 0]) == 3)
    print(s.maximumInvitations([3, 0, 1, 4, 1]) == 4)
    print(s.maximumInvitations([1, 2, 3, 0, 5, 6, 7, 8, 4]))
