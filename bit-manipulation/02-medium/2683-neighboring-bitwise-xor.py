from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        res = 0

        for i in derived:
            res ^= i

        return res == 0

# Explain
# [d1, d2, d3] -> derived
# [x1, x2, x3] -> original
# We have:
# x1^x2 = d1
# x2^x3 = d2
# x3^x1 = d3
# Mean
# x1^x2 ^ x2^x3 ^ x3^x1 = d1 ^ d2 ^ d3
# <=> x1^x1 ^ x2^x2 ^ x3^x4 = d1 ^ d2 ^ d3
# <=> 0 = d1 ^ d2 ^ d3


if __name__ == "__main__":
    s = Solution()
    print(s.doesValidArrayExist([1,1,0]))
    print(s.doesValidArrayExist([1,1]))
    print(s.doesValidArrayExist([1,0]))
