class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
        for i in range(len(s)):
            if s[i] in vowels:
                stack.append(s[i])

        res = ""
        for i in range(len(s)):
            c = s[i]
            if s[i] in vowels:
                c = stack.pop()
            res += c

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.reverseVowels("IceCreAm"))
    print(s.reverseVowels("leetcode"))
