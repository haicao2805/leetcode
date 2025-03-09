class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        res = 0
        for i in range(k - 1):
            colors.append(colors[i])

        N = len(colors)
        start = 0
        end = start + 1
        while end < N:
            if colors[end] == colors[end - 1]:
                start = end
                end = start + 1
                continue

            end += 1

            if end - start < k:
                continue

            res += 1
            start += 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.numberOfAlternatingGroups([0, 1, 0, 1, 0], 3))
    # 0, 1, 0, 1, 0, 0, 1, 0
    # print(s.numberOfAlternatingGroups([0, 1, 0, 0, 1, 0, 1], 6))
    # print(s.numberOfAlternatingGroups([1, 1, 0, 1], 4))
