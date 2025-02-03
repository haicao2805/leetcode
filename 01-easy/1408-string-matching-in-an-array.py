from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res: List[str] = []
        map = {}

        for i in range(0, len(words)):
            for j in range(0, len(words)):
                if i != j and words[i] in words[j]:
                    if not map.get(words[i]):
                        map[words[i]] = True
                        res.append(words[i])

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.stringMatching(["mass", "as", "hero", "superhero"]))
    print(s.stringMatching(["leetcoder", "leetcode", "od", "hamlet", "am"]))
