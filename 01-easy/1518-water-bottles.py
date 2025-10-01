class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles

        while numBottles >= numExchange:
            res += numBottles // numExchange
            exchangedBottles = numBottles // numExchange
            numBottles = exchangedBottles + numBottles - numExchange * exchangedBottles

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.numWaterBottles(9, 3))
    print(s.numWaterBottles(15, 4))
