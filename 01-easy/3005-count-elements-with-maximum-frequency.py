from typing import Counter, List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        if not nums:
            return 0

        freqMap = Counter(nums)
        maxFreq = freqMap.most_common(1)[0][1]
        return sum(freq for freq in freqMap.values() if freq == maxFreq)


if __name__ == "__main__":
    s = Solution()
    print(s.maxFrequencyElements([1, 2, 2, 3, 1, 4]))
    print(s.maxFrequencyElements([1, 2, 3, 4, 5]))
    print(s.maxFrequencyElements([10, 12, 11, 9, 6, 19, 11]))


class VersionOneSolution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        numMap = {}
        for n in nums:
            numMap[n] = 1 if n not in numMap else numMap[n] + 1

        maxOccurrence = max(numMap.values())
        res = 0
        for v in numMap.values():
            if v == maxOccurrence:
                res += v
        return res
