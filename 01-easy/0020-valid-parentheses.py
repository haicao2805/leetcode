class Solution:
    def isValid(self, s: str) -> bool:
        openChar = ['(', '[', '{']
        closeCharMap = {
           ')': '(',
           ']': '[',
           '}': '{'
        }
        stack = []

        for c in s:
            if c in openChar:
                stack.append(c)
            else:
                if not stack or closeCharMap.get(c) != stack[-1]:
                    return False
                else:
                    stack.pop()
        return not stack

if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("([]){}"))
    print(s.isValid("(}"))
    print(s.isValid("([)]"))
    print(s.isValid("]"))
