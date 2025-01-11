from typing import List

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        freq: List[int] = [0] * 26

        for c in s:
           freq[ord(c) - ord('a')] += 1

        sumMod = 0
        for i in range(len(freq)):
            if(freq[i] != 0):
                sumMod += freq[i] % 2

        return len(s) >= k and sumMod <= k

if __name__ == "__main__":
    s = Solution()
    print(s.canConstruct("annabelle", 2))
    print(s.canConstruct("leetcode", 3))
    print(s.canConstruct("aaabbbcdmm", 4))

# annabelle
# a 2
# n 2
# b 1
# e 2
# l 2

# leetcode
# l 1
# e 3
# t 1
# c 1
# o 1
# d 1
