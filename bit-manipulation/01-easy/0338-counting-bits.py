from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)

        for i in range(1, n + 1):
            if i & 1 == 0:
                res[i] = res[int(i / 2)]
            else:
                res[i] =  res[i-1] + 1

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.countBits(2))
    print(s.countBits(5))
