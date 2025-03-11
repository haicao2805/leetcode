from typing import DefaultDict, List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        adj = DefaultDict(list)

        for i in range(N):
            for j in range(N):
                if isConnected[i][j]:
                    adj[i].append(j)

        def dfs(city: int):
            stack = [city]
            while stack:
                city = stack.pop()
                if city in visit:
                    continue
                visit.add(city)
                for ncity in adj[city]:
                    stack.append(ncity)

        res = 0
        visit = set()
        for i in range(N):
            if i not in visit:
                dfs(i)
                res += 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print(s.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
