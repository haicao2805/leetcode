from typing import List


class Solution:  # Neetcode solution
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        edges = [[] for _ in range(numCourses)]
        for [src, dst] in prerequisites:
            if dst not in edges[src]:
                edges[src].append(dst)

        hmap: dict[int, set[int]] = {}

        def dfs(src: int):
            if src not in hmap:
                hmap[src] = set()
                for nei in edges[src]:
                    hmap[src] = hmap[src].union(dfs(nei))
                hmap[src].add(src)
            return hmap[src]

        for i in range(numCourses):
            dfs(i)

        res: List[bool] = []
        for [src, dst] in queries:
            res.append(dst in hmap[src])
        return res


if __name__ == "__main__":
    s = Solution()
    print(
        s.checkIfPrerequisite(
            5, [[0, 1], [1, 2], [2, 3], [3, 4]], [[0, 4], [4, 0], [1, 3], [3, 0]]
        )
        == [True, False, True, False]
    )
    print(s.checkIfPrerequisite(2, [[1, 0]], [[0, 1], [1, 0]]) == [False, True])
    print(s.checkIfPrerequisite(2, [], [[1, 0], [0, 1]]) == [False, False])
    print(
        s.checkIfPrerequisite(3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]])
        == [True, True]
    )


class BruteForceSolution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        hmap = [[] for _ in range(numCourses)]
        for [src, dst] in prerequisites:
            if dst not in hmap[src]:
                hmap[src].append(dst)

        def dfs(src: int, dst: int):
            tmp = False
            for nei in hmap[src]:
                if nei == dst:
                    return True
                tmp = dfs(nei, dst)
                if tmp:
                    break
            return tmp

        res = []
        for [src, dst] in queries:
            res.append(dfs(src, dst))
        return res
