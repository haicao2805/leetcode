import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0:
            return False

        sqrtN = math.sqrt(n)

        log2SqrtN = math.log2(sqrtN)

        return log2SqrtN == int(log2SqrtN)
