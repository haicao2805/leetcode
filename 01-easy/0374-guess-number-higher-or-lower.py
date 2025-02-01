# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

# class Solution:
#     def guessNumber(self, n: int) -> int:
#         l, r = 1, n
#         while l <= r:
#             m = (l + r) // 2
#             res = guess(m)
#
#             if not res:
#                 return m
#             if res == 1:
#                 l = m + 1
#             else:
#                 r = m - 1
#
#         return -1
#
# if __name__ == "__main__":
#     s = Solution()
#     print(s.guessNumber(10))
