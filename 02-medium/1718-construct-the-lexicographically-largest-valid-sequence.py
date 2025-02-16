from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0] * (n * 2 - 1)
        isUsed = [False] * (n + 1)

        def backtrack(curIdx: int, seq: List[int], used: List[bool], n: int) -> bool:
            if curIdx == len(seq):
                return True
            if seq[curIdx] != 0:
                return backtrack(curIdx + 1, seq, used, n)
            for i in range(n, 0, -1):
                if used[i]:
                    continue

                used[i] = True
                seq[curIdx] = i

                if i == 1:
                    if backtrack(curIdx + 1, seq, used, n):
                        return True

                elif curIdx + i < len(seq) and seq[curIdx + i] == 0:
                    seq[curIdx + i] = i
                    if backtrack(curIdx + 1, seq, used, n):
                        return True
                    seq[curIdx + i] = 0
                used[i] = False
                seq[curIdx] = 0

            return False

        backtrack(0, res, isUsed, n)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.constructDistancedSequence(5))
