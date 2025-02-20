from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        N = len(nums)
        uniqueSet = set(nums)

        def backtrack(idx: int, s: str) -> str:
            if idx == N:
                if s not in uniqueSet:
                    return s
                return ""

            add_0 = backtrack(idx + 1, s + "0")
            if add_0:
                return add_0
            return backtrack(idx + 1, s + "1")

        return backtrack(0, "")


if __name__ == "__main__":
    s = Solution()
    print(s.findDifferentBinaryString(["01", "10"]))
    # print(s.findDifferentBinaryString(["00", "01"]))
    # print(s.findDifferentBinaryString(["111", "011", "001"]))
