class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        res = []

        def dfs(curNum):
            if curNum > n:
                return
            res.append(curNum)
            for j in range(10):
                nextNum = curNum * 10 + j
                if nextNum <= n:
                    dfs(nextNum)
                else:
                    break

        for i in range(1, 10):
            dfs(i)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.lexicalOrder(13))
