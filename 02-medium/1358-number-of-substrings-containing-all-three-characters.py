from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hmap = defaultdict(int)

        res, l = 0, 0
        for r in range(len(s)):
            hmap[s[r]] += 1

            while len(hmap) == 3:
                res += len(s) - r
                hmap[s[l]] -= 1
                if hmap[s[l]] == 0:
                    hmap.pop(s[l])
                l += 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.numberOfSubstrings("abcabc"))
    print(s.numberOfSubstrings("aaabc"))
    print(s.numberOfSubstrings("abc"))
