from collections import defaultdict


class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        visited = [False] * n
        res = 0

        for i in range(n):
            connectedComponents = []
            stack = [i]
            visited[i] = True
            while stack:
                node = stack.pop()
                connectedComponents.append(node)
                for nei in graph[node]:
                    if not visited[nei]:
                        stack.append(nei)
                        visited[nei] = True

            isFullyConnected = True
            for node in connectedComponents:
                if len(graph[node]) != len(connectedComponents) - 1:
                    isFullyConnected = False
                    break

            if isFullyConnected:
                res += 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.countCompleteComponents(n=6, edges=[[0, 1], [0, 2], [1, 2], [3, 4]]))
    # print( s.countCompleteComponents(n=6, edges=[[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]))
