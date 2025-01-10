from typing import List

class Solution:
    def isSubset(self, seq: List[int], minSeq: List[int]):
        for i in range(26):
            if(seq[i] < minSeq[i]):
                return False
        return True


    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res: List[str] = []
        minSeq: List[int] = [0] * 26

        for w in words2:
            seq: List[int] = [0] * 26
            for c in w:
                seq[ord(c) - ord('a')] += 1
            for i in range(26):
                minSeq[i] = max(minSeq[i], seq[i])


        for w in words1:
            seq: List[int] = [0] * 26
            for c in w:
                seq[ord(c) - ord('a')] += 1

            if self.isSubset(seq, minSeq):
                res.append(w)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.wordSubsets( ["amazon","apple","facebook","google","leetcode"], ["e","o"]))
    print(s.wordSubsets( ["amazon","apple","facebook","google","leetcode"], ["l","e"]))
