from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        mapA, mapB = {} # 0 mean not exist, 1 mean exist but not use, 2 mean exist and used
        count = 0
        n = len(A)
        res = []

        for i in range(n):
            a, b = A[i], B[i]

            if not mapA.get(a):
                mapA[a] = 1
            if not mapB.get(b):
                mapB[b] = 1

            if a == b:
                if mapA.get(a) == 1 and mapB.get(b) == 1:
                    count += 1
                    mapA[a] = 2
                    mapB[b] = 2
            else:
                if mapA.get(b) == 1:
                    count += 1
                    mapA[b] = 2
                if mapB.get(a) == 1:
                    count += 1
                    mapB[a] = 2

            res.append(count)


        return res

if __name__ == "__main__":
    s = Solution()
    print(s.findThePrefixCommonArray([1,3,2,4],[3,1,2,4]))
    print(s.findThePrefixCommonArray([2,3,1],[3,1,2]))
    print(s.findThePrefixCommonArray([2,2,2],[2,2,2]))
