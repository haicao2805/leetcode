from collections import defaultdict


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atLeastKConsonants(kk: int):
            hmap = defaultdict(int)
            cnt, nonVowelCnt, l = 0, 0, 0
            for r in range(len(word)):
                if word[r] in "aeoui":
                    hmap[word[r]] = hmap[word[r]] + 1
                else:
                    nonVowelCnt += 1

                while len(hmap) == 5 and nonVowelCnt >= kk:
                    cnt += len(word) - r

                    if word[l] in "aeoui":
                        hmap[word[l]] = hmap[word[l]] - 1
                    else:
                        nonVowelCnt -= 1

                    if hmap[word[l]] == 0:
                        hmap.pop(word[l])
                    l += 1
            return cnt

        return atLeastKConsonants(k) - atLeastKConsonants(k + 1)


if __name__ == "__main__":
    s = Solution()
    # print(s.countOfSubstrings("aeioqq", 1))
    # print(s.countOfSubstrings("aeiou", 0))
    # print(s.countOfSubstrings("ieaouqqieaouqq", 1))
    print(s.countOfSubstrings("iqeaouqi", 2))

# 0 i - a: 0, e: 0, i: 1, o: 0, u: 0 | x: 0
# 1 q - a: 0, e: 0, i: 1, o: 0, u: 0 | x: 1
# 2 e - a: 0, e: 1, i: 1, o: 0, u: 0 | x: 1
# 3 a - a: 1, e: 1, i: 1, o: 0, u: 0 | x: 1
# 4 o - a: 1, e: 1, i: 1, o: 1, u: 0 | x: 1
# 5 u - a: 1, e: 1, i: 1, o: 1, u: 1 | x: 1
# 6 q - a: 1, e: 1, i: 1, o: 1, u: 1 | x: 2
# 7 i
#
