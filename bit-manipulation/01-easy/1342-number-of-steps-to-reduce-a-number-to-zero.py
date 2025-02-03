class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        while num:
            res += 1
            if num & 1:
                num ^= 1
            else:
                num >>= 1
        return res


class SimpleSolution:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        while num:
            res += 1
            if num % 2 == 0:
                num = int(num / 2)
            else:
                num -= 1
        return res
