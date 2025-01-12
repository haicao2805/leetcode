class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False

        lockedStack = []
        unlockStack = []

        for i, c in enumerate(s):
            if locked[i] == "0":
                unlockStack.append(i)
            elif c == '(':
                lockedStack.append(i)
            else:
                if lockedStack:
                    lockedStack.pop()
                elif unlockStack:
                    unlockStack.pop()
                else:
                    return False

        while lockedStack and unlockStack and lockedStack[-1] < unlockStack[-1]:
            lockedStack.pop()
            unlockStack.pop()

        if lockedStack:
            return False

        return True
if __name__ == "__main__":
    s = Solution()
    # print(s.canBeValid("))()))", "010100"))
    # print(s.canBeValid("(()())", "111111"))
    print(s.canBeValid("))))(())((()))))((()((((((())())((()))((((())()()))(()", "101100101111110000000101000101001010110001110000000101"))
    print(s.canBeValid("()()))()())(((()((()((()((()()()))(()()((()((()()(((()())))))()((()(()(())((()()((())))))))(())(())))()()()((()())())(()()))((((((())()())())))))())((((()())(())(())()()()(()(()((()))((((()((()((()())(())((((())(())))(()((((())))((()(((((()()))))((((()))))())()))))())",
                       "0111000100000011110100010110101001110111010111110111111011101000100000011101010000110110001100100100100011000001110101101110011000000011111000111111111001011101100000100111010111010000001100011101000110101011001000100100111110110110100101010111111001000010000010010010"))
