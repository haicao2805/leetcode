from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set()

        def dfs(room: int):
            stack = []
            stack.append(room)

            while stack:
                r = stack.pop()
                if r in visit:
                    continue
                visit.add(r)
                for k in rooms[r]:
                    stack.append(k)

        dfs(0)

        for i in range(len(rooms)):
            if i not in visit:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.canVisitAllRooms([[1], [2], [3], []]))
    print(s.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
