from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = []
        colorMap = {}
        ballMap = {}

        for [ball, color] in queries:
            if ball in ballMap:
                prevColor = ballMap[ball]
                colorMap[prevColor] -= 1

                if colorMap[prevColor] == 0:
                    del colorMap[prevColor]

            ballMap[ball] = color
            colorMap[color] = colorMap.get(color, 0) + 1

            res.append(len(colorMap))

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.queryResults(4, [[1, 4], [2, 5], [1, 3], [3, 4]]))
    print(s.queryResults(4, [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]))
    print(s.queryResults(1, [[0, 1], [1, 4], [1, 1], [1, 4], [1, 1]]))
