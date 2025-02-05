class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        idxArr = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                idxArr.append(i)
            if len(idxArr) > 2:
                return False
        return (
            len(idxArr) == 2
            and s1[idxArr[0]] == s2[idxArr[1]]
            and s1[idxArr[1]] == s2[idxArr[0]]
        )
