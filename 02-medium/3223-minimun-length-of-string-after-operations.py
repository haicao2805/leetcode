class Solution:
    def minimumLength(self, s: str) -> int:
        res = len(s)
        hmap = {}
        for c in s:
            hmap[c] = hmap.get(c, 0) + 1

        for v in hmap.values():
            if v > 2:
                res -= v - 1 if v % 2 == 1 else v - 2

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.minimumLength("abaacbcbb") == 5)
    print(s.minimumLength("aa") == 2)
    print(s.minimumLength("aaabbbbccccc") == 4)
