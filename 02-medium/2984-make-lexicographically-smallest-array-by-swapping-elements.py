from collections import deque
from typing import List

# Optimise one
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups: List[deque] = []
        mapNumToGroup: dict[int,int] = {}

        for n in sorted(nums):
            if not groups or abs(n - groups[-1][-1]) > limit:
                groups.append(deque())

            groups[-1].append(n)
            mapNumToGroup[n] = len(groups) - 1

        res = []
        for n in nums:
            groupIdx = mapNumToGroup[n]
            res.append(groups[groupIdx].popleft())

        return res

class OldSolution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        N = len(nums)
        groups = []
        res = []
        mapNumToGroup = {}

        sortedNums = sorted(nums)

        curGroupIdx = 0
        groups.append([sortedNums[0]])
        mapNumToGroup[sortedNums[0]] = curGroupIdx
        for i in range(1,N):
            currentGroup = groups[curGroupIdx]
            numInCurrentGroup = currentGroup[len(currentGroup) - 1]

            if sortedNums[i] - numInCurrentGroup <= limit:
                groups[curGroupIdx].append(sortedNums[i])
                mapNumToGroup[sortedNums[i]] = curGroupIdx
            else:
                curGroupIdx += 1
                groups.append([sortedNums[i]])
                mapNumToGroup[sortedNums[i]] = curGroupIdx

        for n in nums:
            groupIdx = mapNumToGroup.get(n, 0)
            res.append(groups[groupIdx][0])
            groups[groupIdx].pop(0)

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.lexicographicallySmallestArray([1,5,3,9,8], 2))
    print(s.lexicographicallySmallestArray([1,7,6,18,2,1], 3))
