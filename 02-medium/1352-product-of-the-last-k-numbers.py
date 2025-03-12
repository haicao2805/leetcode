class ProductOfNumbers:

    def __init__(self):
        self.preMul = []
        self.size = 0

    def add(self, num: int) -> None:
        if not len(self.preMul) and num != 0:
            self.preMul.append(num)
            self.size = 1
        elif num == 0:
            self.size = 0
            self.preMul = []
        else:
            self.preMul.append(self.preMul[-1] * num)
            self.size += 1

        print(self.preMul)

    def getProduct(self, k: int) -> int:
        if k > self.size:
            return 0
        if k == self.size:
            return self.preMul[-1]

        return self.preMul[-1] // self.preMul[self.size - k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

if __name__ == "__main__":
    productOfNumbers = ProductOfNumbers()
    productOfNumbers.add(3)
    productOfNumbers.add(0)
    productOfNumbers.add(0)
    productOfNumbers.add(8)
    productOfNumbers.add(3)
    print(productOfNumbers.getProduct(1))
    productOfNumbers.add(7)
    print(productOfNumbers.getProduct(5))
    productOfNumbers.add(3)
    # print(productOfNumbers.getProduct(3))
    # print(productOfNumbers.getProduct(4))
    # productOfNumbers.add(8)
    # print(productOfNumbers.getProduct(2))


class TLEProductOfNumbers:

    def __init__(self):
        self.nums = []

    def add(self, num: int) -> None:
        self.nums.append(num)
        return

    def getProduct(self, k: int) -> int:
        res = 1
        N = len(self.nums)
        for i in range(N - k, N):
            res *= self.nums[i]
        return res


class TLE2ProductOfNumbers:

    def __init__(self):
        self.suffMul = []

    def add(self, num: int) -> None:
        self.suffMul.append(num)

        M = len(self.suffMul)
        for i in range(M - 1):
            self.suffMul[i] *= num
        return

    def getProduct(self, k: int) -> int:
        return self.suffMul[-k]
