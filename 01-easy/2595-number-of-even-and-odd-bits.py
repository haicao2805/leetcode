from typing import List

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even, odd = 0, 0
        idx = 0
        while n:
            even += 1 if idx & 1 == 0 and n & 1 == 1 else 0
            odd += 1 if idx & 1 == 1 and n & 1 == 1 else 0
            idx += 1
            n >>= 1

        return [even, odd]

if __name__ == "__main__":
    s = Solution()
    print(s.evenOddBit(50))
    print(s.evenOddBit(2))
