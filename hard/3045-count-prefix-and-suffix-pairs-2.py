from typing import List

class Solution:
    def getHash(self, str) -> int:
        hash = 0
        for i in range(len(str)):
            hash += (ord(str[i]) - 97) * 37 ** (i + 1) % 1_000_000_001
        return hash


    def isPrefixAndSuffix(self, str1: str, str2: str) -> int:
        if len(str1) > len(str2):
            return 0

        hashStr1 = self.getHash(str1)
        # print(str1, hashStr1)
        hashPrefix = self.getHash(str2[0:len(str1)])
        # print(str2[0:len(str1)], hashPrefix)
        hashSuffix = self.getHash(str2[-len(str1):])
        # print(str2[-len(str1):], hashSuffix)

        if hashStr1 == hashPrefix and hashStr1 == hashSuffix:
            print(str1, hashStr1)
            print(str2[0:len(str1)], hashPrefix)
            print(str2[-len(str1):], hashSuffix)
            return 1

        return 0

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        for i in range(0, len(words) - 1):
            for j in range(i + 1, len(words)):
                res += self.isPrefixAndSuffix(words[i], words[j])
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.countPrefixSuffixPairs(["acc","acb","ac","ca","acb"]) == 1)
    # print(s.countPrefixSuffixPairs(["pa","papa","ma","mama"]) == 2)
    # print(s.countPrefixSuffixPairs(["abab","ab"]) == 0)
